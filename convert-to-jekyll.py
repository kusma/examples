from collections import OrderedDict
from shutil import copyfile
from datetime import datetime
import os, json, yaml, argparse

def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)
yaml.add_representer(OrderedDict, represent_ordereddict)

parser = argparse.ArgumentParser()

parser.add_argument("outdir")

parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

# --videos / --no-videos arguments
videos_parser = parser.add_mutually_exclusive_group(required=False)
videos_parser.add_argument('--videos', dest='videos', action='store_true')
videos_parser.add_argument('--no-videos', dest='videos', action='store_false')
parser.set_defaults(videos=True)

args = parser.parse_args()

exampledir = os.path.join(args.outdir, '_examples')
pngdir = os.path.join(args.outdir, 'assets', 'images', 'examples')
mp4dir = os.path.join(args.outdir, 'assets', 'videos', 'examples')

for d in [exampledir, pngdir, mp4dir]:
    if not os.path.exists(d):
        os.makedirs(d)

for entry in os.scandir('examples'):
    if entry.is_dir():
        if args.verbose:
            print(entry.name)

        markdown = open(os.path.join(entry.path, 'example.md')).read()
        data = json.load(open(os.path.join(entry.path, 'example.json')))

        frontmatter = [
            ('layout', 'example'),
            ('title', data['title']),
            ('synopsis', data['synopsis']),
        ]

        if 'publishedAt' in data and len(data['publishedAt']) > 0:
            frontmatter.append(('date',
                                datetime.fromisoformat(data['publishedAt'])))
        else:
            frontmatter.append(('published', False))

        for key in ['tags', 'uxConcepts', 'jsConcepts']:
            if key in data and len(data[key]) > 0:
                frontmatter.append((key, data[key]))

        pngsrc = os.path.join(entry.path, 'media', 'preview.png')
        pngdst = os.path.join(pngdir, entry.name + '.png')
        if os.path.exists(pngsrc):
            copyfile(pngsrc, pngdst)
            frontmatter.append(('preview-image', entry.name + '.png'))

        if args.videos:
            mp4src = os.path.join(entry.path, 'media', 'preview.mp4')
            mp4dst = os.path.join(mp4dir, entry.name + '.mp4')
            if os.path.exists(mp4src):
                copyfile(mp4src, mp4dst)
                frontmatter.append(('preview-video', entry.name + '.mp4'))

        mdpath = os.path.join(exampledir, entry.name + '.md')
        with open(mdpath, 'w') as outfile:
            outfile.write('---\n')
            yaml.dump(OrderedDict(frontmatter), outfile, default_flow_style=False)
            outfile.write('---\n')
            outfile.write(markdown)
