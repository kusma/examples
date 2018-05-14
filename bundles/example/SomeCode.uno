using Fuse;
using Uno;


namespace SomeCode
{
	public class ThisIsATestClass
	{

		public float ThisMethodCalculatesSomething(float f1, float f2)
		{
			var toIllustrateSnippetsFromUno = "Snippets are fun";
			debug_log("WoaaaH");

			for (int i = 0; i < 10; i++)
			{
				debug_log("We dont care about this in our snippet");
			}

			return f1 + f2;
		}
	}
}