## Student Researcher - Chemical Technologies @ RDM Kade

**Author:** Ruben Flinterman

One of my jobs is as a student researcher for Chemical Technologies at RDM kade (also Hogeschool Rotterdam).
This job began as "Project 5/6" which was part of Technical Computer Science. 

**A brief summary of what Chemical Technologies does: <br>**
They develop and improve a mix of chemicals based on certain fruit sugars which changes color if there is a certain chemical nearby.

**A brief summary of what Niko van Ommen and I do: <br>**
Niko and I develop the software which links the color change to an intensity. We do this by creating our own hardware composition with custom written software and a mobile app. 

**The goal:** <br>
The goal is to create and deliver a good research paper for IEEE of which everyone involved is a co-author, including Niko and me. 

<hr>  

**What do I do?:** I currently work on the second version of our flutter application, so I develop in Java and Dart using gradle as the build tool of choice. 
The application is repeatedly tested on Android, although they are not yet automated. This is on the roadmap, after I finish the redo the Bluetooth implementation.

The second version means that it is not written based on the previous version but rather an actual version instead of a rough prototype. 
In my version I focused on better iOS implementation, a notification system and best of all a better UI with better performance.
This is why I keep replacing and removing unnecessary code so the amount of lines written decreases and the simplicity and documentation quality stays high.

An example of code, in this case for our navigation, is:
``` 
class _MyHomePageState extends State<MyHomePage> {
  // Start app on home page (1) and keep tabs on the current page
  int currentPageIndex = 1;

  // Select the page content with switch cases
  Widget _getPage(int page) {
    switch (page) {
      case 0:
        return const ConnectPage();
      case 1:
        return const HomePage();
      case 2:
        return const InfoPage();
      default:
        return const HomePage();
    }
  }

  @override
  // Build the navigation bar with the logic to switch pages if the correct button is pressed
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: NavigationBar(
        // On navigation select
        onDestinationSelected: (int index) {
          // Set correct page by index
          setState(() {
            currentPageIndex = index;
          });
        },
        // Give the navigation a specific style
        backgroundColor: HexColor("#EBEBEB"),
        indicatorColor: HexColor("#D8DBE2"),
        // Highlight the button from the current page
        selectedIndex: currentPageIndex,
        // Add the buttons which we need to press to change pages
        destinations: const <Widget>[
          NavigationDestination(
            selectedIcon: Icon(Icons.add_circle),
            icon: Icon(Icons.add_circle_outline),
            label: 'Connect',
          ),
          NavigationDestination(
            selectedIcon: Icon(Icons.home),
            icon: Icon(Icons.home_outlined),
            label: 'Home',
          ),
          NavigationDestination(
            selectedIcon: Icon(Icons.info),
            icon: Icon(Icons.info_outline),
            label: 'Info',
          ),
        ],
      ),
      // Set the new page content
      body: _getPage(currentPageIndex),
    );
  }
}
```

These lines of code give us the ability to load page content from other files from within the navigation. 
The selected page will also be highlighted in the navigation and is easy to change.