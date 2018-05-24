#!/bin/sh

projects=`find . -maxdepth 3 -type f -iname *.unoproj`
for project in $projects
do
	echo "uno build $@ -- $project"
	uno build "$@" -- $project
done
