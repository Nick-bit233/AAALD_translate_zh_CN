# Basic Gamespaces

> Chapter 3
>
> Architecture is the thoughtful making of space.
>
> ---LOUIS KAHN

> This quote from famous architect Louis Kahn, similar to our own for
> level design, brings us to our next discussion on gamespaces. In
> Chapter 2, we explored some of the practical tools and methods with
> which we will design game levels, from planning on paper to
> constructing level geom- etry in game engines. Now we will discuss
> basic spatial arrangements that will enable us to create better
> gameplay experiences within our game levels. First, you will learn
> about some simple spatial principles from architec- tural design:
> figure-ground, form-void, and others. Next, we will explore his- toric
> gamespaces such as the maze and labyrinth, learning how these ancient
> space types influence modern game structures. From these core explora-
> tions, we will explore other popular spatial types found in modern
> games and discover how they are used to enforce different gameplay
> mechanics.
>
> Lastly, we will consider player point of view and discover what
> advantages and disadvantages are found in first, third, and other
> camera views.
>
> What you will learn in this chapter:
>
> Architectural spatial arrangements Historic gamespace structures
> Spatial size types
>
> Molecule level spaces
>
> **103**
>
> Form follows gameplay with proximity diagrams Hub spaces
>
> Sandbox gamespaces Considerations of camera
>
> Enemies as alternative architecture

## ARCHITECTURAL SPATIAL ARRANGEMENTS

> As with Chapter 2, we will begin with lessons from architecture.
> Whereas we previously focused on tools and techniques that were useful
> in game engine environments, this time we will discuss spatial
> arrangements that can be utilized in games.
>
> Games and architecture differ in the fact that real-world architecture
> must conform to real-world rules. For example, real-world buildings
> must have both an interior and an exterior---with the shape of one
> influ- encing the other. Real-world architecture must also take into
> consider- ation weather, geology, zoning regulations, and structural
> realities. These are not things that gamespaces must deal with. To one
> extreme, this can mean experimental structures such as Atelier Ten
> Architects and GMO Tea Cup Communication, Inc.'s Museum of the Globe,1
> a large elliptical structure formed from cubes floating in space
> (Figure 3.1) or Hidenori Watanave's explorable database sculpture on
> the life of Brazilian archi- tect Oscar Niemeyer2---both former
> structures within the virtual world *Second Life*.3 For more
> day-to-day level design, however, this means gamespaces that are free
> from interior/exterior requirements. This results in more freeform
> spatial layouts based on player movement patterns, narrative events,
> or game mechanics (Figure 3.2). Indeed, *interior* and *exterior* are
> little more than descriptions based on the art used to deco- rate the
> gamespace.
>
> With these differences in mind, spatial designers for games can take
> advantage of architectural lessons within the freedom of game design
> environments. Some of these lessons even have conceptual links to how
> levels are constructed in many modern game engines.
>
> Figure-Ground
>
> The first architectural spatial arrangement we will explore is that of
> *figure-ground*. Figure-ground is derived from artistic notions of the
> *posi- tive* and *negative* space of a composition, where positive
> space describes
>
> ![](./media/media/image165.jpeg){width="3.009688320209974in"
> height="2.7266666666666666in"}
>
> FIGURE 3.1 A sketch of Atelier Ten Architects and GMO Tea Cup
> Communication, Inc.'s Museum of the Globe. Since the building is built
> within a virtual world, it does not require any structure to hold up
> the hundreds of cubes making up its main body. The designers designed
> the building's form in Microsoft Excel and then generated the geometry
> in an automatic modeling program.

![](./media/media/image166.jpeg){width="3.249990157480315in"
height="1.3733333333333333in"}

> FIGURE 3.2 Parti diagram sketches of level plans. Game levels can take
> on unusual formal characteristics because they do not have to conform
> to a corre- sponding interior or exterior as real buildings do.
>
> the area inhabited by the subject of a piece and negative space
> describes space outside of or in between subjects (Figure 3.3).
>
> Figure-ground theory in architecture comes from the arrangement of
> positive space figures, often poche'd building masses, within a nega-
> tive space ground. When viewed in plan, the designer can see how the
> placement of building figures begins to form spaces out of the ground.
>
> ![](./media/media/image167.jpeg){width="1.8603685476815397in"
> height="2.5866666666666664in"}
>
> FIGURE 3.3 This illustration, known as Rubin's vase, shows the concept
> of positive and negative space and how they can be reversed. Based on
> whether the viewer is interpreting the black or white portions of the
> image as the negative space, this is either an illustration of two
> faces looking at one another or of a vase.

![](./media/media/image168.jpeg){width="2.5895538057742784in"
height="1.933332239720035in"}

> FIGURE 3.4 When mapping out spaces with figure-ground drawing, it is
> impor- tant to observe how the positive space figures create spaces
> out of the negative space ground. These spaces, having forms of their
> own, are considered positive space.
>
> Indeed, the formation of such spaces in figure-ground drawings is as
> important as the placement of the figures themselves (Figure 3.4).
> According to architectural designer Matthew Frederick, spaces formed
> by arranged figures become positive space in their own right, since
> they now have a form just as the figures do.4 From an urban design
> standpoint,
>
> these framed spaces are often squares, courtyards, parks, nodes, and
> other meeting areas where people can "dwell," while remaining negative
> spaces are for people to move through.5
>
> Frederick also points out that when utilizing figure-ground, both
> figural elements and spaces can be *implied*,6 either by demarcating a
> space with structural elements or by creating negative spaces that
> resemble the form of nearby figures (Figure 3.5). This echoes
> theoretical neuroscientist Gerd Sommerhoff, who, as quoted by
> architect Grant Hildebrand, said:
>
> The brain expects future event-and-image sets to be event-and- image
> sets previously experienced. When repetition of previous experience
> seems likely, the brain readies itself to reexperience the set. If
> expectances are confirmed, the model is reinforced, with a resultant
> sensation of pleasure.7
>
> In this way, we can see how figure-ground becomes a powerful tool for
> level designers to create additive and subtractive spaces within many
> game engines. Many engines allow for the creation of additive figure
> elements to be arranged within negative 2D or 3D space. Gamespaces are
> often based on mechanics of movement through negative space, using
> positive elements as ledges or supports for a player's journey. Under
> other mechanics, forming spaces in-between solid forms allows for the
> creation of rooms, corridors, and other spaces that players can run,
> chase, and hide in. Additionally, designers can communicate with
> players via implied

![](./media/media/image169.jpeg){width="2.0054166666666666in"
height="2.113332239720035in"}

> FIGURE 3.5 These illustrations show how figure-ground arrangements can
> be used to imply spaces or elements.
>
> ![](./media/media/image170.jpeg){width="3.0in" height="4.28875in"}
>
> FIGURE 3.6 These illustrations show ways that figure-ground
> relationships can be utilized in many gamespaces, implying spatial
> relationships can be an effective way of relaying spatial messages to
> players.
>
> boundaries or highlighted spaces that use figure-ground articulations
> like those described by Sommerhoff (Figure 3.6).
>
> Form-Void
>
> *Form-void* (also called *solid-void*) is in many ways a
> three-dimensional evolution of figure-ground. It is the natural
> application of figure-ground in games where the gamespace will be
> viewed from a non-top-down per- spective (Figure 3.7). In form-void
> theory, spaces that are carved out of solid forms are implied to have
> a form of their own.
>
> Just as figure-ground is spatial arrangement by marking off spaces
> with massive elements, form-void is spatial arrangement by adding
> masses or sub- tracting spaces from them. This further resembles the
> operation of many of
>
> ![](./media/media/image171.jpeg){width="2.527090988626422in"
> height="2.5933333333333333in"}
>
> FIGURE 3.7 Some examples of form-void relationships between forms.
>
> the game engines described in Chapter 2, "Tools and Techniques for
> Level Design," in how these engines allow for the placement of
> geometric forms or for their carving out of an endless mass.
> Similarly, 3D art programs allow for intersections between forms to be
> realized through either careful modeling or *Boolean operations*,
> where mathematical equations are used to combine 3D models in additive
> or subtractive ways. Buildings such as Peter Zumthor's Therme Vals or
> Mario Botta's Casa Bianchi, both in Switzerland, show how form-void
> relationships can be used to carve out spaces for balconies, door-
> ways, windows, private rooms, and other functions (Figure 3.8). In
> games, such additions and subtractions can be used for hidden alcoves,
> secret pas- sages, sniping spots, or even highlighted level goals.
>
> Arrivals
>
> As we have already seen, level design is an art of contrasts. It is
> also an art of sight lines, pathways, dramatic lead-ups, and ambiguity
> about the nature of where you are going. All of these elements
> contribute to the experience of an *arrival*, the way in which you
> come into a space for the first time.
>
> Much of how we will communicate with the player is through arriv- als
> in space. It is also in how that space ushers the player toward his or
> her next destination or provides the means for the player to choose
> his or her own path. Much of how you experience a space when you
> arrive
>
> ![](./media/media/image172.jpeg){width="3.3337489063867016in"
> height="2.293332239720035in"}
>
> Casa Bianchi
>
> FIGURE 3.8 Sketches from Therme Vals by Peter Zumthor and Casa Bianchi
> by Mario Botta show how forms and voids can be used to define space.
>
> in it comes from the spatial conditions of the spaces that preceded
> it: if you are arriving in a big space, spaces leading up to it should
> be enclosed so the new space seems even bigger, light spaces should be
> preceded by dark, etc. In their book *Chambers for a Memory Palace*,
> architects Donlyn Lyndon and Charles W. Moore highlight John Portman &
> Associates' Hyatt Regency Atlanta hotel as featuring such arrival in
> its atrium space. Dubbed the "Jesus Christ spot" by critics, it was
> not uncommon soon after the hotel was built for businessmen to arrive
> in the twenty-two-story atrium from the much lower-ceilinged spaces
> preceding it and mutter "Jee-sus Christ!" as they looked upward.8
> Similar spatial experiences are common in exploration-based games such
> as those in *The Legend of Zelda* or *Metroid* series for leading up
> to important enemy encounters, item acquisitions, or story events
> (Figure 3.9).
>
> Another important element of how players arrive at spaces is their
> point of view from the arrival point. As we will see later in the
> chapter, camera angles in games have a great deal of influence with
> how a player understands space. However, dramatic reveals and arrivals
> are possible regardless of the chosen point of view. In classical
> architecture, the procession-like approach to the Parthenon in Athens,
> Greece, shows how an occupant's point of view is steered toward
> dramatic reveals. Visitors climbing up the steps of the Acropolis
> would first see the Parthenon from below. Then, passing through
>
> ![](./media/media/image173.jpeg){width="3.0in" height="1.85375in"}
>
> FIGURE 3.9 Many games use contrasting spatial conditions to highlight
> the approaches to gameplay-important spaces such as boss rooms or
> goals. This dia- gram of the Temple of Time from *The Legend of Zelda:
> Ocarina of Time*, where the player receives a narrative-important
> sword, shows how contrasted spaces and a Byzantine-esque basilica plan
> emphasize the importance of the sword chamber.
>
> ![](./media/media/image174.jpeg){width="3.6770877077865265in"
> height="2.035in"}FIGURE 3.10 Diagram of the entry procession to the
> Parthenon. Visitors did not approach from the entryway side, but from
> a corner. They then had to walk around the building. Since all
> elevations of the building were equally intricate, it could be enjoyed
> from all sides as visitors walked around to the entrance.
>
> the Propylaea, the portico-like entrance building of the Acropolis,
> they would be greeted by a three-quarters view of the Parthenon from
> its north- western corner rather than a more two-dimensional view from
> straight on. The path then forced visitors to walk around the building
> before they would wind back to the entrance of the Parthenon itself.
> From this forced path, visitors got a more theatric approach to the
> Parthenon than if they had walked straight up to its entrance (Figure
> 3.10).
>
> Genius Loci
>
> A last architectural spatial lesson is less of an arrangement and more
> of another goal for designing your own spaces. This lesson is known as
> *genius loci*, also known as *spirit of place*. This term comes from a
> Roman belief that spirits would protect towns or other populated
> areas, acting as the town's *genius*. This term was adopted by
> late-twentieth-century architects to describe the identifying
> qualities or emotional experience of a place. Some call designing to
> the concept of genius loci *placemaking*, that is, creating memorable
> or unique experiences in a designed space.
>
> In Chapter 2, we discussed the *Nintendo Power* method of level
> design, where the designer creates a macro-scaled parti or plan of his
> or her level, and then distributes highlighted moments of gameplay as
> though developing a map for a game magazine. Each of these highlighted
> moments of gameplay--- be they enemy encounters, movement puzzles, or
> helpful stopping points--- has potential for its own genius loci. Are
> these places for rest or for battle? Should the player feel relaxed,
> tense, or meditative in these gamespaces? The answers to these
> questions depend highly on the game you are building, but can help you
> determine the kind of feel you want for your levels.
>
> Beyond individual gameplay encounters, level designers can implant
> genius loci within the entirety of their gamespaces and use it as a
> tool for moving players from one point to another. Genius loci can be
> built through manipulations in lighting, shadows, spatial
> organization, and the size of spaces, which will all be discussed in
> detail later in the book. If you are building a level for a horror
> game, for example, the genius loci you build should be one of dread,
> created through careful selection of environmental art, lighting,
> sound effects, and other assets. Spaces in a game with little or no
> genius loci can be *circulation* spaces, that is, spaces for the
> player to move through to get to the next destination. Depending on
> the gameplay you are creating, circulation spaces may be a chance to
> rest between intensive encounters or tools for building suspense
> before a player gets to the next memorable gameplay moment.
>
> Now that we have discussed a few more general spatial concepts, we can
> move on to exploring some historical gamespace archetypes. These will
> allow us to take the tools and techniques we have learned thus far and
> employ them in classical gameplay structures.

## HISTORIC GAMESPACE STRUCTURES

> Many games and puzzles have been inspired by spaces described in
> classical literature or built in to historic sites. Beyond defining a
> specific
>
> spatial condition of a game environment, they serve as important
> models for how game worlds can be structured: linearly, branching, or
> interconnected.
>
> Labyrinth
>
> The first of these spaces is the classical *labyrinth.* According to
> Greek legends, the Labyrinth was built by the architect Daedelus to
> hold the half-man half-bull Minotaur for King Minos of Crete.
> Representations of labyrinths in art dating as far back as the Roman
> Empire depict laby- rinths as winding passages that loop around
> themselves, eventually reach- ing an endpoint (Figure 3.11). While
> labyrinths are often confused with branching mazes, artists and
> writers such as Hermann Kern have made the distinction that classic
> labyrinths are *unicursal*---consisting of a single winding path.9
> Labyrinths are also notable for their use as a floor pattern in many
> medieval churches, such as Chartres Cathedral, where walking the path
> of the labyrinth was a meditative experience.
>
> Labyrinths are an important model for understanding gamespaces that
> are navigated in a linear fashion. As Salen and Zimmerman point out,
> games are often the least productive way to accomplish a task.10
> Labyrinths also demonstrate that even in linear gamespaces, both lit-
> eral and gameplay twists, turns, and challenges can add interest to an
> otherwise straightforward pathway. Beyond singular levels, many games
> are themselves labyrinthian, requiring players to follow one set path
> of events. Such a structure is useful for games where an embedded
> narrative, theme, or argument is being communicated to the player.

![](./media/media/image175.jpeg){width="2.0362849956255467in"
height="2.013333333333333in"}

> FIGURE 3.11 An illustration of a classical labyrinth.
>
> Maze
>
> Often confused with unicursal labyrinths, *mazes* are branching
> spatial puzzles where occupants and players must find their way
> through an elab- orate structure of walls and pathways with multiple
> dead ends to find an exit point (Figure 3.12). Due to their branching
> nature, mazes are said to be *multicursal*, having more than one
> defined path. Despite the name, the legend of the Minotaur and the
> Cretan Labyrinth actually describes a maze---thus the current popular
> interchangeability between the terms *maze* and *labyrinth*. Upon
> finishing the structure, Daedelus is said to have nearly gotten lost
> among its many branching paths. Thus the hero Theseus utilized a ball
> of thread to remind himself of the way out during his mission to kill
> the Minotaur.
>
> From the Renaissance through the nineteenth century, architects also
> developed *hedge mazes*, multicursal pathways through tall bushes in
> the gardens of large estates. Originally unicursal labyrinths, these
> structures evolved into branching paths that often contained several
> points of inter- est. Of note is the Labyrinth of Versailles, within
> which explorers could find thirty-nine sculptures depicting Aesop's
> Fables (Figure 3.13). The PC indie title *Slender: The Eight Pages*11
> uses a similar layout, where players must navigate a maze of
> pitch-black forest pathways to find notebook pages before they are
> captured by a malicious entity (Figure 3.14).
>
> Mazes, and even recreations of European-style hedge mazes and their
> American derivative, corn mazes, are a very common spatial type in
> games. Their branching nature with potential dead ends implies a rich
> *risk-reward* structure, where the game asks you to weigh different
> uncer- tain options with the hope of choosing an advantageous answer.
> In terms of game mechanics, maze levels of games are often paired with
> features such as powerful enemies or time limits to create dramatic
> gameplay situations (Figure 3.15).

![](./media/media/image176.jpeg){width="2.8712489063867017in"
height="1.189818460192476in"}

> FIGURE 3.12 An illustration of a maze.
>
> ![](./media/media/image177.jpeg){width="2.5378094925634294in"
> height="3.0533333333333332in"}
>
> ![](./media/media/image178.jpeg){width="4.333748906386702in"
> height="3.0775in"}FIGURE 3.13 A plan of the Labyrinth of Versailles
> showing the many branching paths.
>
> FIGURE 3.14 A map of the forest in *Slender: The Eight Pages*. Notice
> that it has a similar layout and node-based structure for places where
> players may find the titular pages.
>
> ![](./media/media/image179.jpeg){width="2.6126017060367452in"
> height="1.7799989063867017in"}
>
> FIGURE 3.15 Two examples of in-game maze levels from *The Legend of
> Zelda: Ocarina of Time* and *Super Mario Bros 3* show how designers
> use mazes to com- plement dramatic elements such as powerful enemies
> (*Zelda*) or a time limit (*Mario*).
>
> The dead ends in mazes do not always have to be negative. Many games
> with explorable dungeons, such as *Final Fantasy* or *Zelda* titles,
> use branching paths and dead ends as incentives for exploration. Often
> these explorable branches yield treasure or other rewards. Games with
> even simpler worlds can also utilize small branching paths, such as in
> the previously mentioned mobile game *SWARM!*. Within levels of this
> game, small diversionary paths off of a level's typical route can lead
> to caches of coins and other rewards (Figure 3.16).
>
> Rhizome
>
> While *maze* and *labyrinth* are architectural terms, *rhizome* is a
> term from botany. Rhizomes are networks of roots formed by underground
> stems of plants. This term was borrowed by philosophers Gilles Deleuze
> and Félix Guattari for their two-volume work *Capitalism and
> Schizophrenia*. As a philosophical concept, rhizomes describe a
> lateral representative structure of information and data without
> distinctive entry and exit points. At the beginning of *A Thousand
> Plateaus*, Deleuze and Guattari outline the guide- lines of a rhizome,
> the most important of which, for our purposes, is that every point in
> them is connected to every other point at the same time12 (Figure
> 3.17). In this regard, the term *rhizome* has been used to describe
> the Internet,13 as users can access information on any website from
> any other website by typing in its Uniform Resource Locator (URL).
>
> Spatially, the term *rhizome* can apply to any place that can be
> instantly traveled to from any other place. In the real world, air
> travel allows this
>
> ![](./media/media/image180.jpeg){width="3.0026192038495187in"
> height="2.7066666666666666in"}
>
> FIGURE 3.16 A plan sketch of level 1-3 of *SWARM!* showing small
> passageways off of the main level path. While not traditionally
> maze-like, these branching paths demonstrate in a small game the same
> methods for creating player curiosity found in much more complex
> titles.

![](./media/media/image181.jpeg){width="2.6934492563429573in"
height="1.2in"}

> FIGURE 3.17 A diagram of a rhizomatic structure. Mathematically, these
> are referred to as *complete graphs*, where all vertices on a
> geometric object connect to all other vertices. These kinds of
> structures are often used in religious iconogra- phy, such as the
> Christian shield of the trinity59 (also pictured).
>
> to an extent. In games, a popular mechanic in large adventure games is
> to give players access to an instant transportation function that
> allows dis- tances to be traveled quickly. In *Pokémon*, for example,
> players eventually gain an ability that allows bird Pokémon to
> transport them to places they have already visited. This ability also
> exists in many games in *The Legend of Zelda*, *Final Fantasy*, and
> *Elder Scrolls* series to help players manage travel over large
> in-game landscapes.
>
> *ActiveWorlds*,14 *Second Life*, and other large virtual worlds have
> similar functions, but make them part of the user's standard moveset
> by allowing him or her to type in coordinates of where he or she would
> like to go. In *ActiveWorlds*, this has turned locations along the x
> and y axes of the world map, such as points (45, 0) or (0, 45), as
> well as points along the center diag- onal between the two, such as
> (45, 45), into major commerce and devel- opment thoroughfares15 since
> they could be traveled to and remembered easily. Likewise, in *Second
> Life*, the interior of the Museum of the Globe can only be accessed
> through *Second Life*'s coordinate system---further making it a piece
> of architecture that can only exist within a virtual world. The
> ability of game developers to script such options into games makes
> rhizomes a unique option for creating world logic and geometry within
> digital games.
>
> Now that we understand spatial types that can describe the structures
> of both single levels and entire game worlds, we can discuss how even
> more micro-scaled portions of levels can engage users emotionally. For
> this next section, we look particularly at the sizes of gamespaces and
> discover how they affect a player's relationship with a space.

## SPATIAL SIZE TYPES

> While size distinctions for gamespaces seem like rather banal informa-
> tion, they actually create some very interesting emotional scenarios
> in game levels. Here we discuss three size types that level designers
> can use to create their levels. These types can be used in a variety
> of gameplay scenarios, such as contextual tutorials and creating drama
> through survival scenarios.
>
> Narrow Space
>
> The first size type we will discuss is *narrow space*, a spatial
> condition where the occupant feels confined and unable to move.16 When
> consid- ering the measurement techniques highlighted in Chapter 2,
> narrow gamespace is that which is not much larger than a player
> character's own size metrics---often with space for only two of such a
> character to stand in a passageway (Figure 3.18). Narrow space is a
> significant spatial type in video games that can be used for a variety
> of dramatic or skill-based gameplay scenarios.
>
> Narrow spaces create tension by giving space *scarcity*, limited
> amounts such that space itself becomes a valuable resource. Under this
> model, *conflict* can rise from players' drive to keep space for
> themselves from other
>
> ![](./media/media/image182.jpeg){width="3.5362849956255467in"
> height="1.3533333333333333in"}
>
> FIGURE 3.18 Plan diagrams of narrow space. These examples show how
> narrow spaces can be used to create conflict scenarios among players
> and NPCs.

![](./media/media/image183.jpeg){width="3.3433431758530183in"
height="1.6466666666666667in"}

> FIGURE 3.19 Diagram of a typical hallway space in *Resident Evil*'s
> Spencer Mansion. The narrow hallways create a claustrophobic
> environment. This causes enemy encounters to be a significant threat,
> as the player is less able to move around them.
>
> players or non-player characters (NPCs). In player vs. player
> conflicts, narrow space can be used to create bottlenecks for creating
> ambushes and traps or to provide tense "threading the needle" moments
> in racing games. The narrowing of space close to the limits of player
> metrics creates a sense that the player cannot perform many of the
> actions he or she could under other conditions. This is significant
> for the other function of narrow spaces⎯evoking vulnerability by
> limiting player movement options. This is a common design feature of
> many horror games such as *Resident Evil*, where the hallways of the
> Spencer Mansion combined with the game's non-intuitive "tank controls"
> create a heightened sense of claustrophobia
>
> (Figure 3.19).
>
> Stealth games also use narrow space in interesting ways. Games in the
> *Metal Gear Solid* series offer a plethora of spaces to hide in, but
> while some comfortably allow hero Solid Snake to scout out his next
> hiding
>
> ![](./media/media/image184.jpeg){width="3.0035312773403327in"
> height="1.9133333333333333in"}
>
> FIGURE 3.20 Narrow spaces in *Metal Gear Solid* games offer
> concealment from enemies, but at the cost of both mobility and
> visibility.
>
> spot, others, such as lockers, vents, or crawl spaces, limit both
> Snake's mobility and the player's ability to see what is around him
> (Figure 3.20). This feature of many stealth games reinforces the idea
> that in stealth games, as in horror games, player characters are often
> weaker than their opponents.
>
> Intimate Space
>
> The next size type is known as *intimate space*. Intimate spaces are
> neither confining nor overly large17 and are, in fact, what one might
> call *metric appropriate*, at a size that comfortably supports the
> size and movement metrics of player characters (Figure 3.21). Within
> intimate spaces, interac- tive surfaces or features are within reach
> of a player character's inherent abilities. In some games, the amount
> of space described in this way may change if the abilities of player
> characters can expand through additions such as high-jump capabilities
> or others.
>
> A great deal of gamespaces could be described as intimate space. In
> corridor shooters and in multiplayer arenas where players are on even
> ground with no significant vantage points above or below, the
> gamespace can be considered *multilateral intimate space* (Figure
> 3.22). In multiplayer situations, intimate spaces create a spatially
> even playing field shared by multiple actors. Player skill
> notwithstanding, no player has an advantage over any other. Racing
> game tracks with wide enough road space for mul- tiple cars allow
> players to compete against one another for race position rather than
> track space. In these situations, contrasting narrow and inti- mate
> spaces creates interesting gameplay situations and allows players to
> build strategies of how to proceed.
>
> ![](./media/media/image185.jpeg){width="2.5037456255468067in"
> height="2.2466666666666666in"}
>
> FIGURE 3.21 Intimate spaces are ones where everything within the space
> is accessible by the player character with its inherent abilities.

![](./media/media/image186.jpeg){width="3.0063396762904637in"
height="1.8333333333333333in"}

> FIGURE 3.22 This sectional diagram shows multiplayer shooter
> characters bat- tling within an intimate space arena. Architectural
> features like ramps, slight elevation changes, and occasional barriers
> do not interrupt the spatially even playing field of the level.
>
> Intimate spaces in single-player games can have several beneficial
> effects. Due to their comfortable accessibility, they are often
> "friendly" locations within the plot of a game. Princess Peach's
> Castle from *Super Mario 64* is an intimate space because the player
> can access many of the platforms inside without putting Mario at any
> significant risk. There are no pits or enemies to endanger the
> character and end the game. This space and others like it also act as
> a *tutorial space* for the game, allowing players to experiment with
> Mario's abilities at their own pace.
>
> ![](./media/media/image187.jpeg){width="2.667074584426947in"
> height="2.9in"}
>
> FIGURE 3.23 Intimate spaces in *Batman: Arkham Asylum* involve the use
> of vantage points and sight lines that are accessible through the
> abilities of the player character, Batman. These abilities allow for
> greater use of the level space by players than enemies, so intimate
> space in this case provides spatial advantages for this single-player
> experience.
>
> One game series that utilizes intimate space in interesting ways is
> the *Batman: Arkham* series. For the first game in the series,
> *Batman: Arkham Asylum*, developer Rocksteady coined the term
> *predator gameplay* to describe the game's stealth hunting. As a
> contrast to typical stealth games where the protagonist is somehow
> weaker than the enemies, the developer argued, Batman would be
> stronger and have better command of his surroundings, similar to his
> capabilities in the *Batman* comic books.18 To complement Batman's
> abilities of gliding, grappling, and silently taking down foes, the
> level designers created level spaces that enabled these actions, with
> high van- tage points and sight lines that allowed the player to
> capitalize on Batman's unique abilities (Figure 3.23). Unlike
> multiplayer games, where the focus of intimate space is to create
> comfortable spaces for many players, single-player games can utilize
> intimate spaces to give players an advantage over foes.
>
> Prospect Space
>
> At times, games put players in the positions that Batman's foes in
>
> *Arkham Asylum* find themselves in: wandering through a large open
>
> space and open to attack. This third spatial size type is known as
> *prospect space* (Figure 3.24).19 Hildebrand describes prospect space
> as that in which humans had to historically find food, water, and
> other necessities---outside of the safety of caves and open to
> predators and the elements.
>
> Prospects in gamespaces take many forms. Once again looking to the
> multiplayer map, prospects are found in any area where one player may
> take a spatial advantage over another, such as by having a vantage
> point from above. In single-player games, prospects are used as *boss
> rooms*: large open spaces where the player cannot use his or her
> abilities to take a spatial advantage but must instead fight a single
> powerful foe. Such spaces are used regularly in the *Mega Man* game
> series, where players must finish each level by battling a powerful
> Robot Master (Figure 3.25).

![](./media/media/image188.jpeg){width="3.003872484689414in"
height="1.6266666666666667in"}

> FIGURE 3.24 This illustration shows a basic idea of how prospect space
> operates in terms of a player's openness to enemy attack.

![](./media/media/image189.jpeg){width="2.5054593175853017in"
height="1.8866655730533683in"}

> FIGURE 3.25 Boss rooms in the *Mega Man* series are often large and
> open so players must directly deal with the attacks of foes.
>
> Prospect spaces are similar to narrow spaces in their potential for
> creating fear in the player. They do so through opposite means,
> however. If narrow spaces create a sense of claustrophobia, prospects
> create a sense of *agoraphobia*, an anxiety disorder that includes a
> fear of wide-open spaces. While there may be a general sense of
> vulnerability in prospect spaces of a multiplayer deathmatch map, this
> feeling can be heightened through the use of fog, music, shadows, and
> other atmospheric effects related to the forming of your gamespace's
> genius loci. *Slender: The Eight Pages*'s entire environment is a
> prospect draped in pitch-black darkness, heightening the sense that
> the malevolent Slender Man has mastery of the gamespace and is waiting
> just beyond the player's field of vision. His artificial intel-
> ligence (AI) is scripted in such a way that he will randomly appear to
> the player at varying distances and move closer when the player is
> looking away (Figure 3.26). As such, Slender Man's movements across
> the pros- pect space give the impression that he is supernatural and
> can move great distances quickly. To put this in terms of movement
> metrics: the space is built to enhance Slender Man's metrics while it
> makes the player's own movement metrics seem agonizingly slow.
>
> Prospect spaces and the other spatial size types are much more complex
> beyond the qualities listed here. In later chapters, we discuss how
> they are

![](./media/media/image190.jpeg){width="3.1670548993875767in"
height="2.326304680664917in"}

> FIGURE 3.26 In *Slender: The Eight Pages*, the antagonist spawns
> randomly around the player, demonstrated in this plan diagram, giving
> the impression that he has complete control over the pitch-black
> prospect space (locations 1, 2, and 3 on the diagram). If the player
> turns away, the antagonist quickly pursues and further gives the
> impression of great speed (location 4).
>
> mixed and matched with other types of spaces to create dramatic
> spatial articulations. Next, however, we explore a spatial type that
> connects the singular spatial atoms that we have thus far discussed.

## MOLECULE LEVEL SPACES

> Now that we have discussed several isolated gamespace types, we need
> to understand how to link these spaces together in interesting and
> meaning- ful ways. Designers Luke McMillan and Nassib Azar, who is
> himself a for- mer architect, in their Gamasutra article "The Metrics
> of Space: Molecule Design,"20 highlight a methodology for spatial
> organization based on the arrangement of gamespaces, how players reach
> one from another, and how designers can allow or disallow access
> between them for interesting play scenarios. Based on interpretations
> of mathematical graphing theory, which we delved into briefly during
> our discussion of rhizomes, they call this methodology *molecule
> design*. In this section, we discuss the basics of molecule design and
> adapt it to the architectural concepts we have explored thus far.
>
> The Basics of Molecule Design
>
> McMillan and Azar's concept of molecule design is primarily focused on
> the relationship between play spaces, treated in their graphs as
> *nodes* and *edges*. Nodes are the play spaces themselves---areas with
> significant enemy encounters, item pickups, spawn points, or
> opportunities for action. Edges describe the relationship between
> these spaces, be they visual or spatial (as in you can travel from one
> to another). One addition implied in McMillan and Azar's article is
> that of *visual language*, that we can formally add for our purposes
> to the diagrams to dictate what the proximities between nodes and the
> size or nature of your edges mean. In Figure 3.27, dotted lines show
> that spaces are viewable from one another, and solid lines show that
> you can move from one to another. Arrows on the solid lines show if
> spaces are one way, and thick lines show that spaces between the nodes
> are direct paths. Level plan and section drawings are included to show
> a level space that may be designed from such a molecule.
>
> This methodology greatly resembles the *Nintendo Power* method dis-
> cussed in Chapter 2, but engages spatial design on a more conceptual
> level. It is important to note that the shapes of these molecules are
> not neces- sarily the layout of the level, but a description of how
> spaces interact with one another. To demonstrate this, Figure 3.28
> shows another set of level drawings that can be derived from the
> molecule diagram in Figure 3.27.
>
> ![](./media/media/image191.jpeg){width="3.8759765966754154in"
> height="6.543303805774278in"}3
>
> FIGURE 3.27 This molecule diagram establishes links between nodal
> gamespaces with the use of edges. A visual language has been
> established for edges to help describe elements of
> three-dimensionality as shown in the accompanying plan and section
> drawings of the level.
>
> ![](./media/media/image192.jpeg){width="4.326676509186352in"
> height="5.430555555555555in"}FIGURE 3.28 This set of level drawings is
> derived from the same molecule diagram found in Figure 3.27. Molecules
> describe relationships rather than actual level space.
>
> Understanding the abstract nature of molecule diagrams is impor- tant
> for utilizing McMillan and Azar's last important concept: *Steiner
> points*. In graph theory, a *Steiner tree* is a spatial puzzle where
> the player must find the shortest point between two lines, constructed
> from points labeled A, B, and C, where A connects to B, B connects to
> C, but C does not connect to A. In McMillan and Azar's example, the
> answer
>
> to the puzzle is a slight cheat, where players can draw a node
> directly in the middle of the three that is connected to each. This is
> a Steiner point (Figure 3.29). Steiner points in level design can
> occur in any spatial scenario where a player may access play spaces
> vertically, that is, by climbing or jumping from a nodal gamespace to
> a Steiner point space, then into another nodal gamespace in the
> molecule diagram (Figure 3.30). Steiner points are essentially
> shortcuts in level paths. These can be utilized purely by jumping from
> high ledges onto lower

![](./media/media/image193.jpeg){width="1.9251268591426072in"
height="0.939070428696413in"}

> FIGURE 3.29 This diagram shows the Steiner tree puzzle and the answer
> utiliz- ing a Steiner point.

![](./media/media/image194.jpeg){width="3.34875in"
height="2.8649989063867016in"}

> FIGURE 3.30 Steiner points in level design may be used to
> conceptualize secrets, or shortcuts. These diagrams of tracks from
> *Mario Kart 64* show how Steiner points (and some considerable skill)
> may be employed to skip large portions of the game's two longest
> tracks.
>
> ones to save time, or may even be incentivized with power-ups or other
> rare items.
>
> Now that we have discussed the basics of McMillan and Azar's mol-
> ecule design principles, we will see how we can further integrate them
> with our own architectural approach.
>
> Spatial Types as Molecule Nodes and Edges
>
> Molecule diagrams are very abstract. As such, they leave a lot of
> guess- work about what could be used as a significant gameplay node.
> We have already discussed many spatial principles that can be useful
> for defin- ing these spaces. In the previous chapter, we established
> that in level design, form often follows core mechanics. Likewise,
> nodal gamespaces in your own molecule diagrams can represent areas
> where the player employs unique or intense applications of your core
> mechanics: big gun fights, sharp turns, boss battles, difficult
> platforming, etc. These nodes are also opportunities to emphasize the
> genius loci of your level. To once again use *Slender: The Eight
> Pages* as an example, each landmark in the wooded maze carries its own
> experience unique from the rest of the course. In the infamous
> bathhouse, for example, the normally prospect- structured space of the
> game world suddenly becomes a maze of nar- row hallways where Slender
> Man could be around any corner. While the transitional edges between
> such landmark nodes allow for encounters with Slender Man, they
> ultimately shuffle players between more notable gameplay nodes.
>
> *Slender* also demonstrates an important distinction of using spatial
> types as nodes. While the game itself is structured as a
> Versailles-esque maze, several of the nodes contain their own smaller
> maze spaces. The circulation spaces that bring players from one node
> to another may be very linear, as may the nodes themselves. In a level
> prototype based on Washington, D.C.'s, Sackler Gallery of Art, an
> underground museum with a downward-spiraling ramp system, the
> transitional spaces utilize the downward ramps to take players from
> one intense gamespace to another. In the more intense sections were
> either unicursal corridors that would use atmospheric effects or tight
> mazes for enemies, in this case zombies, to inhabit (Figure 3.31).
>
> Molecule diagrams may also describe spaces where spatial size changes
> significantly. As described previously, size changes create their own
> special gameplay scenarios. McMillan and Azar pay special atten- tion
> to *spawn points* in their article: the spaces where players begin a
>
> ![](./media/media/image195.png){width="3.6804615048118987in"
> height="1.8933333333333333in"}
>
> FIGURE 3.31 This image of a prototyped level shows how transitional
> spaces (the downward spiraling ramps) may be linear, while the nodal
> gamespaces may follow their own linear or branching pathways on a
> smaller scale.
>
> level or come back to life during multiplayer matches. These spaces
> may be large but intimate, allowing players to gather resources before
> rejoining battles. Likewise, transitional spaces may be equally inti-
> mate, keeping players on an even playing field when inside, but lead-
> ing to large prospect spaces where players may gain spatial advantage
> over one another (Figure 3.32). In single-player games, where players
> can often better admire the designs of levels, transitions from
> intimately or narrowly scaled circulation to prospect spaces may not
> only describe changes in gameplay intensity, but also create their own
> "Jesus Christ spot" experiences.
>
> If one reverses this dynamic, prospect-scaled transitional spaces
> allow for the generous usage of Steiner points. In the previous
> Sackler Gallery level prototype, the entire circulation space is a
> Steiner point that players may utilize within the limits of the player
> character's ability to fall from heights without taking damage.
> Alternatively, *Metroid Prime 2: Echoes* utilizes prospect/circulation
> spaces as challenges. The Steiner point ability to jump from higher
> levels to lower ones is used as an obstacle in sec- tions where
> players must scale a set of platforms to progress in the game (Figure
> 3.33). Later, if the player is returning from the higher gamespaces,
> the Steiner point becomes a shortcut again.
>
> In the next section, we explore another diagram type similar to mol-
> ecule diagrams, though much less abstract. These diagrams will help us
> determine how to join related gameplay events already outlined for
> levels to one another.
>
> ![](./media/media/image196.jpeg){width="4.274998906386702in"
> height="3.23712489063867in"}![](./media/media/image197.jpeg){width="3.7536942257217847in"
> height="2.537693569553806in"}FIGURE 3.32 This drawing and molecule
> diagram of a multiplayer map from *Halo 4* shows how players move from
> intimate hallway spaces into prospect nodes where they may gain
> strategic advantages over one another.
>
> FIGURE 3.33 This drawing of the Agon Wastes environment from *Metroid
> Prime 2: Echoes* and the accompanying molecule diagram show how
> Steiner points are used as obstacles: failure to jump to platforms
> where one may progress results in a return to earlier areas.

## FORM FOLLOWS GAMEPLAY WITH PROXIMITY DIAGRAMS

> When a property owner wants to build a building, he or she often
> outlines a *building program* to give to potential architects. The
> program is a list of necessary functions the building must perform and
> spaces the build- ing must have. Similarly, in Chapter 2, we discussed
> how level designers begin their design with a vision of the types of
> gameplay experiences it should have. This form follows function
> approach allows us to relate our level designs to the mechanics of the
> games we are designing them for.
>
> Molecule design diagrams, which we discussed in the previous section,
> are very similar to a diagram type that architects use to orga- nize
> building program requirements into building spaces: *proximity
> diagrams*. Proximity diagrams, like molecule diagrams, are made up of
> bubbles and connected with lines. The bubbles represent rooms or
> spaces that are to be part of the building and are sized according to
> square footage requirements for these spaces. Likewise, lines connect-
> ing the bubbles are sized according to how important it is for them to
> be adjacent21 (Figure 3.34). Also like molecule diagrams, proximity
> dia- grams are not actual spatial plans. They are a tool for analyzing
> the functional idea for a building, but should not be understood as
> its final spatial plan.22

![](./media/media/image198.png){width="2.0in" height="2.53625in"}

> FIGURE 3.34 A building proximity diagram. Each bubble is sized
> according to the required square footage of a space. The sizes of
> lines show the necessity of spaces being adjacent in the final
> building.
>
> ![](./media/media/image199.jpeg){width="4.180555555555555in"
> height="3.201388888888889in"}
>
> FIGURE 3.35 A proximity diagram for a multiplayer first-person shooter
> (FPS) level. In this example, it is important for each sniper position
> to have a view of the main competition area for each spawn point to
> have access to gear. Despite the layout of the diagram, the final
> design can (and should) look drastically different.
>
> Proximity diagrams can be used for level design as they would be used
> for real-world architecture. Rather than each bubble having the name
> or square footage for a functional building space, they have the names
> of gameplay spaces in them, such as boss room, sniping spot, or finish
> line. The sizes of these bubbles can stand for their size type. The
> sizes and type of line used to connect the bubbles can describe
> proximity priority and the type of connection spaces have. For
> example, it may be important for snip- ing positions to have a view of
> a large prospect space in a map, even if the player must actually
> travel a long set of corridors to get there (Figure 3.35). Now that we
> have looked at some methods for organizing spaces in levels, we will
> explore some common world configurations found in games
>
> to discover how they are organized for ease of use and enjoyment.

## HUB SPACES

> Beyond the spatial and organizational concepts already discussed,
> there exist other spatial types that deserve consideration. The first
> of these are *hub spaces.* Hubs are a type of intimate space where the
> player may
>
> ![](./media/media/image200.jpeg){width="4.166679790026246in"
> height="2.0606102362204726in"}
>
> FIGURE 3.36 Hub levels include spaces such as Princess Peach's Castle
> from *Super Mario 64* and Station Square in *Sonic Adventure*. They
> both lead players from environment to environment while allowing them
> to backtrack and freely explore.
>
> access a game's different levels. Many hubs are non-threatening and
> offer players the ability to explore within the metrics of their
> character's abili- ties. Hubs distinguish themselves from other game
> world structures, such as sandboxes, which we discuss later, by
> separating levels from more intense gamespaces through the use of
> portals, doors, or some other device (Figure 3.36).
>
> Hubs became popular in 3D games like *Super Mario 64* and *Banjo
> Kazooie* as a way to facilitate player travel between different
> environ- ments. In this way, they are semi-rhizomatic: they offer a
> central point from which to jump from gamespace to gamespace. From a
> performance standpoint, these hubs allow levels to be loaded one at a
> time rather than create the level of seamlessness that one might
> expect in a large sandbox environment. Also, they offer a narrative
> "out" for games that wish to have characters travel to themed worlds
> such as ice, volcano, jungle, etc. when it would otherwise be
> illogical.
>
> From a gameplay standpoint, hubs are notable for how they manage
> player goals. Hub-based games are typically structured around
> collecting resources, gold stars, puzzle pieces, etc., that facilitate
> travel through the game world and unlock portals. As players complete
> more intense gameplay challenges, they collect more of the unlocking
> resources and can access new levels. While hub-based games offer an
> overall labyrinthine model through the general order in which one
> engages levels, they also offer great freedom to players in
> determining what missions to take, when and if to backtrack, or how
> long they wish to explore each level (Figure 3.37).
>
> ![](./media/media/image201.jpeg){width="1.88375in" height="3.4825in"}
>
> FIGURE 3.37 This diagram shows how hub-based games are typically
> struc- tured. They represent a ladder of sorts where the overall
> journey is linear, but the activity of how to overcome each rung is
> largely determined by the player.
>
> In many ways, hubs offer the best of both linear and open styles of
> gameplay. In the next section, we will explore another type of space
> that offers players almost complete freedom over their gameplay
> experience.

## SANDBOX GAMESPACES

> In single-player games, developers create the feeling of a large open
> world by utilizing *sandbox* gamespaces. Sandbox worlds are named for
> their ability to have defined boundaries but also allow players to
> play however they want in less structured ways than many other games
> allow. One might imagine that the design of sandbox worlds is simple:
> provide the player with a large open set of spaces in which to play,
> and give him or her things to do. However, large spaces carry with
> them the problems of user orientation and location awareness.
>
> As many real-world spatial designers know, these are problems regu-
> larly encountered by urban planners. It is perhaps not surprising that
> many of the most popular sandbox worlds are themselves cities. In this
>
> section, we will explore some urban design principles that can be used
> to build successful sandbox spaces.
>
> Pathfinding with Architectural Weenies
>
> Perhaps one of the most important elements of sandbox spaces comes
> from creative pioneer Walt Disney. While shooting live action films
> with dogs, his studio would often need them to run across the set. To
> accomplish this, they would use sausages, which Disney called weenies,
> to entice the ani- mals to run in the direction they wanted. Disney
> described tall buildings in his parks as having a similar effect for
> patrons by assisting with direc- tional orientation. Jesse Schell,
> author of *The Art of Game Design: A Book of Lenses* and one of the
> designers on *Pirates of the Caribbean: Battle for Buccaneer Gold*,
> used the term *architectural weenie* to describe landmarks used to
> attract players to goal points in their game.23
>
> Architectural weenies are an integral part of sandbox spaces. They
> allow these worlds to retain their openness but still direct players
> to places that designers want them to go. Many designers, such as
> Scott Rogers, cite Disneyland and its twin, the Magic Kingdom, as
> inspiration for much of their level design knowledge. In the design of
> Disneyland, Sleeping Beauty Castle, Splash Mountain, and other
> attractions not only direct visitors to themselves, but allow them to
> understand where they are by using these elements as guide points. In
> *Grand Theft Auto IV*'s24 take on Liberty City, landmarks like the
> Statue of Happiness and Rotterdam Tower serve simi- lar functions:
> directing players to them but also acting as guideposts while
> wandering the landscape. In Schell's examples, the term
> *architectural* is used to describe how level designers create not
> only designed building spaces, but also designed natural spaces, as
> *Battle for Buccaneer Gold* uses volcanoes, burning towns, and other
> attention-getting sights. Schell's des- ignation of these objects also
> shows how architectural weenies can take many forms beyond tall
> buildings.
>
> One game that cleverly uses architectural weenies is *Half-Life 2:
> Episode 2.* In one scene, players must use a radio to alert allies of
> an impending alien attack. The narrative sequence of this scene
> requires play- ers to enter a building to determine that the radio
> both exists and cannot power up. Then, players must explore a nearby
> building to find the power source for the complex and switch it on
> (Figure 3.38). To keep the open feel of the landscape while directing
> player action, the developers textured the radio building with bright
> red and yellow hues and textured the larger tower building in drab
> browns. Despite its smaller size, this turned the
>
> ![](./media/media/image202.png){width="3.6278193350831147in"
> height="0.8834995625546807in"}![](./media/media/image203.png){width="3.6278193350831147in"
> height="0.8858748906386702in"}![](./media/media/image204.png){width="3.6278193350831147in"
> height="0.8858748906386702in"}![](./media/media/image205.png){width="3.6278193350831147in"
> height="0.4417497812773403in"}![](./media/media/image206.png){width="0.11651356080489939in"
> height="0.11486001749781277in"}![](./media/media/image207.png){width="0.12294400699912511in"
> height="0.11666557305336833in"}![](./media/media/image208.png){width="0.11550634295713036in"
> height="0.11606846019247594in"}FIGURE 3.38 A plan of the radio tower
> complex in *Half-Life 2: Episode 2*. While smaller, the radio building
> is textured with brighter colors that contrast with the greens and
> blues of the landscape. This directs player attention to it first,
> rather than the dark browns of the radio tower building itself.
>
> radio building into an architectural weenie by making it stand out
> more against the natural greens, blues, and browns of the wooded
> landscape.25 Clearly, architectural weenies can take a multitude of
> forms. They can also serve a variety of tasks, including directing
> player action and helping players better navigate gamespace. In the
> next section, we will explore how this concept and others can further
> help players navigate sandbox worlds.
>
> Organizing the Sandbox: Kevin Lynch's Image of the City
>
> As stated previously, finding one's way in a large open space can be
> daunt- ing. For this reason, urban planners have developed a number of
> organiza- tion principles for how to structure urban spaces. In his
> influential book *The Image of the City*,26 urban planner Kevin Lynch
> reports the results of a five-year study of how people form mental
> maps of cities. From this study, Lynch advocates aiding visitors by
> organizing cities with these ele- ments: landmarks, paths, nodes,
> districts, and boundaries. Organizing cities in this way creates what
> he calls *legibility* for observers of a city,27 which is what we
> should strive to achieve in our own sandbox gamespaces.
>
> This section will look at each of these elements to understand how
> they may be applied to video game sandbox spaces.
>
> *Landmarks*
>
> *Landmarks* are recognizable elements that can be guideposts to people
> in an urban space.28 This definition should sound very similar to the
> concept of architectural weenies, as they are the same thing. As we
> discussed in the previous section, landmarks not only call attention
> to themselves, but also allow players to orient themselves by
> observing their relationship to the landmark in space. As many games
> do not utilize just urban-themed sand- box worlds---with popular
> choices including fantasy, post-apocalyptic, or historic
> landscapes---these landmarks can be natural objects or human- made
> elements that contrast with the rest of the landscape.
>
> *Half-Life 2* utilizes landmarks in an interesting way different from
> how they are typically used in sandbox games. While not a sandbox game
> itself, *Half-Life 2* strives to create the feeling of a large,
> seamless world by dividing levels with minimal fanfare: no menus,
> cutscenes, or other con- spicuous scene transitions. The game
> establishes early on that a distant tower, the Citadel, is the home
> base of the game's villains, and that the player's final goal is to
> eventually reach and destroy it (Figure 3.39). This tower is visible
> from most levels in the game, and players can track their progress by
> observing how close they are to the structure.

![](./media/media/image209.jpeg){width="3.336839457567804in"
height="2.2in"}

> FIGURE 3.39 The Citadel in *Half-Life 2* is a useful landmark for
> players to under- stand not only where they are in the game's large
> world, but also how far they have progressed in the game itself. The
> game establishes early on that its climax will take place there.
>
> The Citadel shows how versatile landmarks are. They can direct player
> action, allow them to orient themselves in a large sandbox space, or
> track their progress by measuring their proximity to them.
>
> *Paths*
>
> We have already discussed circulation spaces, channels for travel that
> con- nect significant gamespaces. Lynch discusses these types of
> spaces in his book as *paths*.29 Paths in urban design include roads,
> sidewalks, and other thoroughfares that allow people to travel through
> the city.
>
> In terms of molecule design, these paths are the lines that connect
> sig- nificant gamespaces. They can have their own challenges, but are
> often intimately scaled spaces without significant aesthetic features.
> Their pur- pose is to usher players through to the next point of
> important game- play. In our previous example of Liberty City, paths
> are the same types of spaces---streets, sidewalks, etc.---as those
> suggested by Lynch.
>
> On the other hand, games like *The Elder Scrolls V: Skyrim* do not
> repre- sent their sandboxes as large urban spaces, but as open
> landscapes. As such, many of the paths between towns, dungeons, and
> forts are much less direct and are, in fact, open fields. This allows
> players to enact their own Steiner points by taking direct routes
> between landmarks. While these paths might not be explicitly designed
> as such, they are recognizable. However, they run the risk of getting
> the player lost in their vast openness. To mitigate this, designers
> use subtle geographic features such as dirt paths, signposts, or
> rivers to evoke more direct pathways represented in urban plans.
>
> For designers working in engines such as those described in Chapter 2,
> keeping these guidelines in mind when working with tools such as in-
> engine terrain editors is important for creating worlds that are not
> just aesthetically attractive, but also usable.
>
> *Nodes*
>
> In many urban spaces, the intersections of pathways offer a variety of
> opportunities for engaging users. Not only can they be their own guide
> points for navigation (such as when you direct someone to a business
> by telling them what corner it is on), but they can also be places for
> people to gather or interact (Figure 3.40). Lynch calls these
> intersections *nodes* and highlights how they can be important focal
> points for large networks of paths.30
>
> Nodes can be locations for landmarks to reside, channeling different
> paths onto one end goal. They can also, as Lynch points out, be
> strategic
>
> ![](./media/media/image210.jpeg){width="3.2545188101487312in"
> height="1.8733333333333333in"}
>
> Logan Circle Washington DC
>
> Star Junction Liberty City
>
> FIGURE 3.40 Nodes at the intersections of paths offer opportunities
> for players to make strategic choices of where to go next in a game
> world and interact with NPCs or other players that may be gathered
> there.
>
> *decision points*31 at which observers can decide what path to take
> next. In many open-world games such as *Skyrim*, such decision nodes
> are every- where, forcing players to prioritize how they wish to spend
> their time: do you want to go find things to do in a town or explore
> dungeons?
>
> These decisions become even more interesting when they take on moral
> or narratological purposes. For example, Rockstar Vancouver's high
> school-themed sandbox game *Bully*32 allows players to explore the
> fictional town and private school campus, taking on missions for
> various cliques in the school. The reputation the player has with each
> clique---bullies, jocks, nerds, greasers, and preppies---forms the
> game's morality system. If the player does something to impress the
> nerds, he or she may lose the favor of the jocks, etc. Spatially, the
> game offers many nodes at which the player can not only interact with
> NPCs, but also choose clique-friendly locations such as the gym,
> library, or autoshop (Figure 3.41).
>
> *Edges*
>
> Edges, according to Lynch, are boundaries not formed by paths. They
> are linear elements that mark a transition from one continuous area or
> condi- tion to the next. Edges can be walls, rows of buildings,
> changes in vegeta- tion, or other markers that show that an area has
> changed in character or genius loci.33 In sandbox games, areas of
> varying genius loci allow players to feel that the world has variety
> in the way that games with distinct level theme types---ice, fire,
> forest, etc.---have (Figure 3.42).
>
> ![](./media/media/image211.jpeg){width="3.667498906386702in"
> height="3.58375in"}FIGURE 3.41 The grounds immediately outside the
> Bullworth Academy school building in the game *Bully* are a node that
> offers access to a number of land- marks important to the game's
> various cliques. The academy building itself is a landmark that also
> serves as an architectural weenie, allowing players to orient
> themselves by their spatial relationship to it.

![](./media/media/image212.jpeg){width="3.2385017497812774in"
height="2.1533333333333333in"}

> FIGURE 3.42 Different types of edges in sandbox worlds.
>
> In 1949, mythologist Joseph Campbell described the hero's journey
> monomyth in his book *The Hero with a Thousand Faces*.34 As summarized
> by Campbell, the hero's journey plays out in this manner:
>
> A hero ventures forth from the world of common day into a region of
> supernatural wonder: fabulous forces are there encountered and a
> decisive victory is won: the hero comes back from this mysterious
> adventure with the power to bestow boons on his fellow man.35
>
> In *Origins of Architectural Pleasure*, architect Grant Hildebrand
> con- siders a spatial version of the monomyth focused on the journey's
> *mate- riality*. Materiality is the understanding of textural and
> visual qualities of a surface. As applied to the hero's journey,
> Hildebrand notes that as the hero ventures from his world, the
> materiality of his surroundings change from that of comfort, to epic
> wilderness, and often to a dark, corrupted state when encountering the
> final enemy.36 One sees this pattern play out in numerous works of
> literature, film, and games: from *Beowulf* 37 to *The Legend of
> Zelda*.
>
> From a production standpoint, edges can mark a change in *art style*.
> The type of architectural or vegetation models you use can shift,
> signify- ing the change to a new area. Likewise, transitions between
> textures on surfaces can generate player-perceived edges. These
> transitions can be quick or gradual. A quick transition may mark a
> defined border, and can often be accompanied by architectural details
> such as walls or gates, as landscape rarely transitions suddenly.
> These are especially useful if the area you are entering is the site
> of an event---a battle, fire, alien encounter, etc.---or if you are
> transitioning the realm of a specific group. Gradual transitions, on
> the other hand, may help build anticipation for reaching a new zone.
> Burned trees, arrows, and other ammunition sticking out of the
> scenery, etc., can give the impression that you are about to enter a
> dangerous area, creating a tension when approaching it. They can also
> indicate that you are reaching a natural border between environment
> types⎯plains to forest, desert to canyon, etc.
>
> *Districts*
>
> The last of Lynch's elements is the *district*, which he describes as
> sections of a city where the observer enters "inside of" and which
> have some iden- tifying character.38 In the previous section, we
> discussed how changes in art style, environment art elements, and
> texture can indicate changes in
>
> ![](./media/media/image213.jpeg){width="1.8288746719160105in"
> height="1.7982075678040246in"}
>
> FIGURE 3.43 A theoretical game map showing districts.
>
> environments within a sandbox world. Once past these edges, players
> find themselves within districts (Figure 3.43).
>
> Beyond changes in style, districts in games differentiate themselves
> from one another with changes in gameplay: types of NPCs, enemies,
> events, or mini-games. Districts can be containers for distinct
> narrative events or gameplay challenges. In the example of Disneyland,
> the park is divided into distinct districts: Tomorrowland,
> Fantasyland, Frontierland, and others that have their own distinct
> character and set of themed attrac- tions. Likewise, *Grand Theft Auto
> IV*'s Liberty City has several distinct districts of its own: the
> Algonquin district features skyscrapers and night- clubs, while Broker
> is a relatively poor district where the player first inter- acts with
> several of the city's criminals.
>
> If sandbox worlds do not have distinct districts, or if districts do
> not have their own unique gameplay elements, sandbox worlds can feel
> empty. In the unfortunate case of Santa Destroy from the game *No More
> Heroes*,39 the city has many landmarks but few distinct areas of town.
> Instead, the entire city is a South Los Angeles-styled environment
> with a few disparate shops and locations to explore and take on
> missions. The game's action stages, on the other hand, occur in more
> distinct linear environments separated from this sandbox world. As
> reviewer Mark Bozon pointed out, "If the game was based only on the
> open world style, it would have been a pretty sizable
> disappointment."40 If the unique character of the game's action levels
> were carried over to the sandbox world, the city might have not only
> been more fun to explore, but also more believable as an urban space.
>
> Clearly, a successful sandbox world is based on how well a player can
> "read" and understand it. In many games, as in real-world architec-
> ture, lines of sight and understanding the point of view of players
> are of
>
> the utmost importance. What, however, is the designer to do with the
> spatial lessons we have discussed---largely based on real-world
> first-person points of view---if a game is in the third person, or
> even in two dimen- sions? In the next section, we will discuss how a
> player's point of view impacts gamespace.

## CONSIDERATIONS OF CAMERA

> Since the release of the German driving game *Nurburgring 1*41 in 1975
> and its American counterpart *Night Driver*42 in 1976, first-person
> games have been a part of the gaming landscape. However, it was not
> until the early 1990s and the release of id Software's *Wolfenstein
> 3D*43 that first-person games grew to the dominance they hold today.
> Indeed, many first-person games prior to *Wolfenstein* had abstract
> vector graphics or had to show static images rather than displaying a
> real-time textured 3D environment. Meanwhile, other games utilized 2D
> viewpoints from the side of the player character, known as *side
> scrolling* (Figure 3.44), or from above the player character, known as
> *top down* (Figure 3.45), to show the action of a game.

![](./media/media/image214.jpeg){width="3.3320319335083113in"
height="1.5999989063867017in"}

> FIGURE 3.44 A 2D side-scrolling game. The view could be said to be a
> section of the gamespace.

![](./media/media/image215.jpeg){width="2.6667935258092736in"
height="1.3133333333333332in"}

> FIGURE 3.45 A 2D top-down game. The view could be said to be a plan of
> the gamespace.
>
> ![](./media/media/image216.jpeg){width="2.098999343832021in"
> height="3.446665573053368in"}
>
> FIGURE 3.46 A 2D axonometric game.
>
> There were even axonometric (popularly called *isometric*) games such
> as
>
> *Zaxxon*44 and *Q\*Bert*45 (Figure 3.46).
>
> In many modern game engines, point of view is dependent on where the
> designer places the *camera*, an object from which the player views
> gameplay. In a first-person game, the camera is located on a player
> object and given scripts that allow the player to look around freely.
> In a 2D game, the camera looks from either the top or side and often
> has options for perspective turned off, giving the camera an
> *orthographic* view. Axonometric and isometric views often feature
> cameras that look down on the player from up high. In this section, we
> will discuss how camera placement offers different limitations and
> opportunities for how gamespace is viewed.
>
> 3D Views
>
> As most modern games are 3D, and since architecture is most often
> experienced by visitors in a three-dimensional fashion, we will dis-
> cuss 3D views in games first. The two most popular viewpoints for 3D
> games are from the first-person view and the *third-person view*,
>
> where the camera is located outside of the player character's body.
> While the difference between these two viewpoints is often minimal,
> there are gameplay situations better suited to one or the other, which
> we will explore here.
>
> *First Person*
>
> First-person games are those where the camera is located in the "head"
> of the player character mesh (if the game uses a defined mesh for the
> player character at all) and action is viewed from the character's eye
> level. This is the most natural game view, as it is the view from
> which we view our own world (Figure 3.47).
>
> It is in first-person games where level designers have full use of
> many of the architectural concepts discussed in this book. It is also
> where design- ers must use the most architectural tricks to capture
> players' attention, as the player has control over where the camera is
> looking, unlike in other game types. In *Half-Life 2*, for example,
> designers had to find ways to keep players near narrative events where
> NPCs were talking, since the game does not use passive cutscenes.
> Indeed, during narrative events and gameplay, designers must create
> lines of sight to direct player attention to details or direct their
> movement. The exterior contours of a gamespace are not visible from
> this point of view, so spatial size types, architectural weenies, and
> other design arrangements must be used to usher players through the
> gamespace.
>
> From a gameplay perspective, first-person games can be very immer-
> sive, allowing the player to better take on the role of the game's
> protago- nist. There are things that can also be limiting in
> first-person views, such as platform jumping and melee fighting
> mechanics that often benefit from a wider perspective.

![](./media/media/image217.jpeg){width="3.678588145231846in"
height="1.26in"}

> FIGURE 3.47 Cameras in first-person games are located at the eye level
> of a player character and allow for maximum use of sight lines.
>
> *Third Person*
>
> Third-person games are those in which the viewport camera is placed
> somewhere outside of the player character's body. Even among third-
> person games, there are many different varieties of view types. The
> first is *rotating camera*, which has the camera move around the
> player either in or out of his or her control. The second is *behind*,
> where the camera stays at a fixed point behind the player, typically
> by making the camera a *child object* of the player object. The third
> is *over-the-shoulder*, a semi-hybrid of first and third person where
> the camera is close behind the player charac- ter and allows the
> player to move the camera to look where the character is looking
> (Figure 3.48).
>
> Third-person games offer many of the same spatial opportunities as
> first-person games, most notably the ability to create full 3D
> environments where lines of sight and other visual tricks can be used
> to direct player attention. They also offer opportunities to play with
> a camera's sense of perspective: by changing viewing angle options
> that many game engine third-person cameras have, designers can get
> trippy Tim Burton-esque angles and perspectives46 (Figure 3.49).
> Third-person cameras are also used in *fixed-perspective* games such
> as *Resident Evil*47 or *Killer 7* 48 to create cinematic camera
> angles: shots from below, in front, close up, or others. These can
> greatly increase the dramatic effect of certain scenes, though often
> come at the cost of ease of control of the player character.
>
> Third-person games offer additional opportunities for 3D game types
> that first-person games often struggle with. The most notable is
> platform jumping, since the player can see where the player
> character's feet will land. Designers often add a shadow underneath
> the player character to

![](./media/media/image218.jpeg){width="2.3856802274715663in"
height="1.8038188976377953in"}

> FIGURE 3.48 Three common types of third-person perspective in games.
>
> ![](./media/media/image219.png){width="3.24291447944007in"
> height="1.8333333333333333in"}
>
> FIGURE 3.49 In this screenshot from the short game *The Nightmare Over
> Innsmouth*, prepared for a presentation at the Game Developers
> Conference (GDC) in China, the designer modified the camera lens angle
> to get a warped perspective effect.
>
> further help players find their way, such as in *Super Mario 64*. This
> is even more helpful in games with more acrobatic platforming, such as
> *The Prince of Persia: Sands of Time*,49 where players can take time
> to line their character up with poles, swings, ledges, and other
> obstacles that the Prince can climb on. This game also features
> brawler-style melee combat where players must move in and out of
> groups of enemies, something that would be difficult to do in first
> person.
>
> Third-person games suffer in the area that first-person games excel
> in: aiming. Camera AI is also notoriously difficult to code well, so
> cameras that "want to kill players" are a common problem in
> third-person games. Over-the-shoulder third person mitigates this to a
> point, though some line-of-sight spatial relationships are better
> understood in first person.
>
> 2D Views
>
> Before good-looking 3D was technologically possible, 2D games domi-
> nated the industry. Visually, a textured surface in 2D was more
> believable than the vector-generated surfaces of many early 3D games.
> In terms of mechanics, many of the things one can do in a 3D game can
> be done in a 2D game: platform jumping, shooting, exploration, and
> others. Since the heyday of 2D was when gaming devices were not
> powerful enough to create realistic graphics, 3D games were long
> considered to have a presentational advantage over 2D games. Now, as
> 2D games are being revisited on mod- ern gaming technology, they are
> home to presentational styles that mimic hand-made arts such as
> painting, sculpting, crafts, and even knitting.
>
> Games viewed at a 2D perspective have an interesting ability that most
> 3D games do not: showing the player things that are beyond the
> eyesight of the player character. In the *Metroid* series, it is
> common for players to see an upgrade hidden in several feet of rock
> waiting to be claimed, though the player character would logically
> have no idea it is there. This technique is very similar to the one
> employed by director Alfred Hitchcock to create *suspense* in his
> films.
>
> A favorite example of Hitchcock's was to propose a scene where two
> people were sitting at a table, but the camera pans down to show that
> a bomb is underneath. That the diners do not know of the impending
> doom instills the scene with suspense for the audience that does get
> to see the bomb.51 The game *Metroid Fusion*52 utilizes this when an
> evil clone of heroine Samus Aran, the SA-X, walks through a hallway
> that is below the player. While Samus herself would possibly be able
> to hear the footsteps of the clone, the player gets a suspenseful view
> of how nar- rowly he or she is escaping death (Figure 3.50). Sadly,
> this technique is underused in 2D games, though there are other
> view-specific techniques that apply to the two most popular types of
> 2D views: side scrolling and top down.

![](./media/media/image220.jpeg){width="3.084374453193351in"
height="2.8481244531933507in"}

> FIGURE 3.50 The *Metroid* series uses 2D perspectives to show players
> the loca- tion of hidden items and passages. Likewise, *Metroid
> Fusion* uses this perspective to create Hitchcock-esque scenes of
> suspense.
>
> *Side-Scrolling Space*
>
> Side-scrolling gamespaces are ones viewed from the side of the player
> character as though looking at a building section. Side scrollers can
> be some of the most spatially limiting level types, as there is not
> much one can design in the way of pathfinding. One's location in a
> side-scrolling level can also be difficult to track, especially in
> large open-world 2D games, typically termed Metroidvania for their
> popularity in the *Metroid* and *Castlevania* series.
>
> The simplicity of side scrollers makes them effective at teaching
> their own mechanics: they put everything the player needs to know in a
> screen- shot's distance from his or her avatar. Side-scrolling games
> often deal with action best understood from a "to the side" point of
> view, such as jump- ing, climbing, flying, and shooting. As such, it
> is important that when designing side-scrolling levels, there are very
> few "leaps of faith" that the player must take. Even large pitfall
> obstacles must show you their other end in one screenshot's width from
> the side where the player is standing (Figure 3.51). It is important
> for side scrollers to practice their own type of *visual level
> metrics*. Beyond simply making obstacles easily understand- able,
> enemies and enemy projectiles should always leave enough time from
> when they enter the screen to when they reach the player such that the
> player has a chance to see and avoid them (Figure 3.52).
>
> Unfortunately, side scrollers render many of the pathfinding and
> orientation methods we have discussed thus far useless. There are
> some, however, that experiment with not only height and width, but
> also depth by putting 2D level environments in layers that can be
> moved through forward and backward. Games such as *Shantae: Risky's
> Revenge*53 utilize this to give in-game villages a more realistic
> feel. Mazes in this game are more complex, as the player must not only
> move through left/right (x) and up/down (y) axes, but also
> forward/backward (z) (Figure 3.53).

![](./media/media/image221.jpeg){width="3.173856080489939in"
height="1.28in"}

> FIGURE 3.51 In 2D side scrollers, designers should avoid adding "leaps
> of faith" to their games and always allow players to see the other
> side of obstacles from within one screen's width.
>
> ![](./media/media/image222.jpeg){width="3.677292213473316in"
> height="1.4466655730533684in"}
>
> FIGURE 3.52 Enemies and their projectiles in 2D side scrollers should
> leave enough time from when they enter the screen to when they reach
> the player so that the player has a chance to avoid them.

![](./media/media/image223.jpeg){width="2.8694706911636048in"
height="1.7133333333333334in"}

> FIGURE 3.53 Many environments in *Shantae: Risky's Revenge* allow the
> player to move forward and backward through layers of 2D
> side-scrolling environments. These add another level of depth to
> in-game mazes and dungeons not common in many side-scrolling games.
>
> *Top-Down Space*
>
> Top-down gamespaces are ones where gameplay is viewed from above the
> player character as though looking at a building plan. Indeed, many
> early games resembled maps and building plans. On one hand, top-down
> games offer little in terms of creating sight lines and other things
> that are common in 3D games. However, they excel at creating
> opportunities for orientation, as many gamespaces can be understood in
> plan. These spaces can be understood as following the cardinal direc-
> tions of north, south, east, and west, so devices like landmarks allow
> players to find their way through large gamespaces (i.e., "I am north
> of Hyrule Castle").
>
> ![](./media/media/image224.jpeg){width="2.5027810586176726in"
> height="2.486665573053368in"}
>
> FIGURE 3.54 Like side-scrolling games, top-down games can show players
> things that the player character cannot necessarily see.
>
> Like side scrollers, top-down games share the potential for Hitchcock-
> style suspense due to their ability to show players things that the
> player character cannot necessarily see (Figure 3.54). Also like side
> scrollers, enemies should leave enough time between appearing on
> screen and when they hit the player such that the player has a chance
> to move.
>
> Top-down games often feature mechanics that are best enacted in an
> expansive world, such as exploring or interacting with NPCs, though
> there are certainly exceptions. Top-down games, like side scrollers,
> are also well suited to mechanics that involve lining the player
> character up with a tar- get such as shooting, sword fighting, or even
> rudimentary jumping. On the other hand, top-down games tend to be less
> reliant on reaction-based action than side scrollers, so more
> environmental information can be held off screen (Figure 3.55). In
> fact, withholding the entirety of a landscape or architectural feature
> in a top-down gamespace may actually invite players to explore
> further.
>
> Now that we have explored the opportunities present in both 3D and 2D
> game views, we will look at those present in a type of gamespace that
> straddles the line between the two.
>
> Axonometric/Isometric Views
>
> In the early 1980s, developers utilized a new game view type---the
> axono- metric game---to create the impression of 3D space while
> utilizing art that
>
> ![](./media/media/image225.jpeg){width="3.0019739720034995in"
> height="2.153332239720035in"}
>
> FIGURE 3.55 Since many top-down games involve exploring expansive
> worlds, information can be withheld off screen from players. Giving
> players incomplete information, such as showing part of a landmass or
> river in one screenshot, invites players to explore further.
>
> was still actually 2D. Following early axonometric games like *Zaxxon*
> and *Q\*Bert*, this view continued to be popular in games from *Knight
> Lore*54 to *Starcraft*.55 In games, this point of view is often
> referred to as *isometric*, as that is the type of axonometric
> projection used to create the game art.
>
> In classic axonometric games, the game is typically viewed without
> perspectival distortion, that is, without the objects on screen viewed
> along sight lines that meet at a vanishing point. While purely
> axonometric images can create a dramatic 3D effect, they also come at
> the cost of depth perception for the player. Axonometric drawings are
> notorious for the creation of optical illusions such as that shown in
> Figure 3.56. When constructing axonometric gamespaces, it is important
> to show the *vertical relationships* between surfaces very clearly so
> players are not confused by an object's position in space. Likewise,
> it is important to *occlude*, or disable the rendering of, foreground
> objects in these spaces so players do not lose their character when
> they move behind structures.
>
> *Isometric* as a term has also been adopted by modern 3D game devel-
> opers to describe a camera that is positioned at an angle above the
> player character looking down, with perspective options enabled on the
> camera object itself. This type of perspective is actually described
> as *three-point perspective*, as edges meet not only at horizontal
> vanishing points com- mon to two-point perspective, but also at a
> vertical vanishing point below the level. Unlike actual isometric or
> axonometric views, changes in height
>
> ![](./media/media/image226.jpeg){width="2.250673665791776in"
> height="3.013333333333333in"}
>
> FIGURE 3.56 Axonometric drawings can easily disorient the player if
> not drawn properly. When making these kinds of gamespaces, make sure
> you find ways to show vertical spatial relationships.
>
> are easily perceived thanks to the perspective option of the camera.
> This type of view, in both classic and 3D versions, allows for both a
> detailed 3D environment and the designer to show the player things
> that the player character cannot see.
>
> Axonometric views can make it difficult for players to orient them-
> selves in space. Unlike top-down 2D views, the player cannot benefit
> from the use of cardinal directions. And since the camera is facing
> downward, they also cannot make use of sight lines, so as much
> informa- tion should be on screen as possible, unless the world is an
> expansive one similar to those found in top-down 2D games. However,
> isometric games allow designers to make dramatic use of spatial size
> types, as players can easily see how their character relates to the
> environment around them. Still possible is creating a sense of
> claustrophobia with narrow spaces or a sense of agoraphobia with
> prospect spaces. In fact, these spaces' three- point perspective allow
> for the use of rhythmically arranged vertical ele- ments to create a
> sense of *epic hugeness* in prospect spaces---creating a sense of
> *vertigo* as the player looks from the camera down at his or her
> character (Figure 3.57).
>
> ![](./media/media/image227.jpeg){width="2.7501662292213473in"
> height="2.278943569553806in"}![](./media/media/image228.jpeg){width="0.9176520122484689in"
> height="2.7308880139982503in"}![](./media/media/image229.jpeg){width="2.7501662292213473in"
> height="0.4574442257217848in"}
>
> FIGURE 3.57 In this screenshot, regularly spaced biotanks are used in
> this lab environment to create a sense of vertigo from the camera down
> to the player character. This emphasizes the verticality of the
> gamespace, even though the player is viewing the game from a
> third-person perspective.
>
> Now that we have discussed camera views and how they correlate with
> player perceptions of space in games, we will explore one last basic
> spatial concept. This concept will help us take an element unique to
> games and utilize it to toy with how a player perceives the nature of
> space around him or her in games.

## ENEMIES AS ALTERNATIVE ARCHITECTURE

> In *Chambers for a Memory Palace*, Lyndon and Moore describe the con-
> cept of *allies*: statues, short columns, and other architectural
> elements that are of similar scale to an occupant.56 Beyond
> iconographic significance, they point out that allies in a piece of
> architecture can make spaces more inviting. In games, non-player
> characters fulfill many of these functions and often have their own
> gameplay reason for being in a space, sending the player on quests,
> guarding doorways, etc. NPCs that instigate quests often prohibit
> players from moving through a space until specific tasks are
> accomplished. As such, NPCs can help designers drive player
> interaction with the game world.
>
> One key difference between gamespaces and real architecture is that
> enemies, not just allies, can also inhabit gamespaces. Enemies offer
> level
>
> designers a unique type of architectural ally in their antagonistic
> relation- ship with the player. Where friendly NPCs may simply block a
> space until the player helps them, enemies block spaces by threatening
> to damage the player. As the player cannot directly pass through
> enemies without risk- ing damage, game enemies can be seen as
> *alternative architecture*. In the train station environment at the
> beginning of *Half-Life 2*, alien soldiers are used as alternative
> architecture. While many games use locked or non- interactive doors to
> show a player they cannot enter a room, *Half-Life 2* places sentries
> throughout a train station. If the player tries to pass, he or she is
> shoved back. Further attempts by the unarmed player are met with the
> aliens brandishing their weapons, an effective deterrent. Using
> interactive enemies rather than plain locked doors does several impor-
> tant things for the game: it builds *Half-Life 2*'s dystopian
> narrative without exposition, it directs player movement through the
> station, and it creates the feeling that this station is populated,
> just as Lyndon and Moore argue is the role of architectural allies.
>
> Using enemies as architectural elements of a level can be a powerful
> tool for level designers when paired with narrow space as well. In the
> original *Resident Evil*, for example, zombies fill the narrow
> hallways of the Spencer Mansion. As they approach players, they block
> off progress through hallways while shrinking the space the player can
> safely occupy. Players in this situation must decide whether to risk
> running past the zombie or shoot it.
>
> As the *Resident Evil* zombies demonstrate, even enemies with sim- ple
> AI can be powerful spatial tools. In his essay "The Rules of Horror:
> Procedural Adaptation in *Clock Tower*, *Resident Evil*, and *Dead
> Rising*," Matthew Weise describes a concept he calls the *shrinking
> fortress* in zombie films.57 In shrinking fortress scenarios, such as
> the one in *Night of the Living Dead*,58 the protagonists are
> surrounded by a large group of enemies, which continually advance on
> them and capture once-safe ter- ritory. In *Night of the Living Dead*,
> for example, survivors fight to protect themselves within a farmhouse.
> Eventually, the first floor of the house is overrun, and the heroes
> must retreat into the basement. This scenario can play out in games
> through story events that cut off previously acces- sible areas.
>
> An even more powerful application of the shrinking fortress can occur
> in real time. Strong or difficult-to-kill enemies may be used to
> *herd* the player where the designer would like him or her to go
> (Figure 3.58). For this tactic to work, the enemies should be in
> overwhelming numbers, have
>
> ![](./media/media/image230.jpeg){width="1.9724989063867016in"
> height="2.63875in"}
>
> FIGURE 3.58 Enemies may be used to herd players where designers want
> them to go. For this to work, a large number of difficult-to-kill
> enemies should be used.
>
> powerful attacks, or be difficult to kill. A scenario like this often
> requires the level space itself to be large, though swarms of enemies
> will create the feeling of narrow space. Applications like these
> demonstrate the power that level designers have to use enemies, NPCs,
> and other game elements not traditionally viewed as architecture for
> architectural purposes.

## SUMMARY

> In this chapter, we have explored some basic spatial types that we can
> use to form our game worlds. From micro-scaled articulations of
> additive and subtractive space to world structures such as sandboxes,
> hubs, and clas- sic gamespaces, we now have a set of spatial
> configurations to create with the game engine tools discussed in
> Chapter 2. We also know how to cater gamespace to the kinds of
> gameplay experiences we wish them to house through spatial size types.
> To pace these elements out or study how they interact with one
> another, we can utilize molecule and proximity diagrams. We can also
> organize large worlds of gameplay through urban design prin- ciples.
> On the player end, we can cater player experiences of our gamespaces
> to the point of view they will have through in-game cameras. Lastly,
> we can use not only friendly NPCs, but also enemies to populate our
> game worlds, enhance the spatial types we have discussed, and direct
> player action.
>
> In Chapter 4, we will discuss more directly how to create game levels
> that teach the mechanics of a game to players and reinforce these
> mechan- ics through the entirety of a game.

## ENDNOTES

1.  Watanave, Hidenori. Archidemo: The Museum of the Globe. Archidemo.
    <http://archidemo.blogspot.com/2008/07/museum-of-globe.html>
    (accessed February 20, 2013).

2.  Watanave, Hidenori. Archidemo: Oscar Niemeyer in Second Life.
    Archidemo.
    <http://archidemo.blogspot.com/p/oscar-niemeyer-in-second-life.html>
    (accessed February 20, 2013).

3.  *Second Life*. Linden Research (developer and publisher), June
    23, 2003. Online virtual world.

4.  Frederick, Matthew. *101 Things I Learned in Architecture School*.
    Cambridge, MA: MIT Press, 2007, p. 3.

5.  Frederick, Matthew. *101 Things I Learned in Architecture School*.
    Cambridge, MA: MIT Press, 2007, p. 6.

6.  Frederick, Matthew. *101 Things I Learned in Architecture School*.
    Cambridge, MA: MIT Press, 2007, p. 4.

7.  Hildebrand, Grant. *Origins of Architectural Pleasure.* Berkeley:
    University of California Press, 1999, p. 95.

8.  Lyndon, Donlyn, and Charles Willard Moore. *Chambers for a Memory
    Palace*. Cambridge, MA: MIT Press, 1994, p. 212.

9.  Borries, Friedrich von, Steffen P. Walz, and Matthias Böttger.
    *Space Time Play Computer Games, Architecture and Urbanism: The Next
    Level*. Basel: Birkhauser, 2007.

10. Salen, Katie, and Eric Zimmerman. *Rules of Play: Game Design
    Fundamentals*. Cambridge, MA: MIT Press, 2003, p. 97.

11. *Slender: The Eight Pages*. Parsec Productions (developer and
    publisher), June 26, 2012. PC game.

12. Deleuze, Gilles, and Félix Guattari. *A Thousand Plateaus:
    Capitalism and Schizophrenia.* Minneapolis: University of Minnesota
    Press, 1987.

13. Koh, Chuen-Ferng. Chapter 1: Internet-Rhyzome. *Internet: Toward a
    Holistic Ontology*.
    <http://wwwmcc.murdoch.edu.au/ReadingRoom/VID/jfk/thesis/> ch1.htm
    (accessed February 26, 2013).

14. *ActiveWorlds*. ActiveWorlds (developer and publisher), 1997. Online
    virtual world.

15. Jakobsson, Mikael. Activity Flow Architecture: Environment Design in
    ActiveWorlds and EverQuest. In Borries, Friedrich von, Steffen P.
    Walz, and Matthias Böttger. *Space Time Play Computer Games,
    Architecture and Urbanism: The Next Level*. Basel: Birkhauser, 2007,
    pp. 164--167.

16. Totten, Christopher W. Designing Better Levels Through Human
    Survival Instincts. Gamasutra---The Art & Business of Making Games.
    [http://www.](http://www/)
    gamasutra.com/view/feature/6411/designing_better_levels_through\_.
    php?print=1 (accessed February 27, 2013).

17. Totten, Christopher W. Designing Better Levels Through Human
    Survival Instincts. Gamasutra---The Art & Business of Making Games.
    [http://www.](http://www/)
    gamasutra.com/view/feature/6411/designing_better_levels_through\_.
    php?print=1 (accessed February 27, 2013).

18. *Batman: Arkham Asylum* Video---Silent Knight Challenge Mode
    Extended Cut \| GameTrailers. GameTrailers.
    <http://www.gametrailers.com/videos/>
    dfhan4/batman\--arkham-asylum-silent-knight-challenge-mode-extended-
    cut (accessed February 27, 2013).

19. Hildebrand, Grant. *Origins of Architectural Pleasure.* Berkeley:
    University of California Press, 1999, p. 22.

20. McMillan, Luke, and Nassib Azar. Gamasutra---Features---The Metrics
    of Space: Molecule Design. Gamasutra.
    <http://www.gamasutra.com/view/>
    feature/184783/the_metrics_of_space_molecule\_.php (accessed
    February 27, 2013).

21. White, Edward T. *Space Adjacency Analysis: Diagramming Information
    for Architectural Design*. Tucson, AZ: Architectural Media, 1986.

22. Yatt, Barry D. Assessing Program. In *Parti Planning: A Guide to
    Pre-Design Analysis*. Draft ed. Washington, DC: Catholic University
    of America, 2006, chap. 7, 7-35--7-54.

23. Salen, Katie, and Eric Zimmerman. *Rules of Play: Game Design
    Fundamentals*. Cambridge, MA: MIT Press, 2003, p. 353.

24. *Grand Theft Auto IV*. Rockstar North (developer), Rockstar Games
    (pub- lisher), 2008. Xbox 360 game.

25. *Half-Life 2: Episode 2*. Valve Corporation (developer and
    publisher), 2007. PC game. Developer commentary.

26. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960.

27. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960, p. 2.

28. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960, p. 48.

29. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960, p. 47.

30. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960, p. 47.

31. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960, p. 72.

32. *Bully*. Rockstar Vancouver (developer), Rockstar Games
    (publisher), 2006. Playstation 2 game.

33. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960,

> p\. 47.

34. Campbell, Joseph. *The Hero with a Thousand Faces*. 2nd ed.
    Princeton, NJ: Princeton University Press, 1968.

35. Campbell, Joseph. *The Hero with a Thousand Faces*. 2nd ed.
    Princeton, NJ: Princeton University Press, 1968, p. 23.

36. Hildebrand, Grant. *Origins of Architectural Pleasure*. Berkeley:
    University of California Press, 1999.

37. Heaney, Seamus. *Beowulf: A New Verse Translation*. New York:
    Farrar, Straus, and Giroux, 2000.

38. Lynch, Kevin. *The Image of the City*. Cambridge, MA: MIT Press,
    1960, p. 47.

39. *No More Heroes*. Grasshopper Manufacture (developer), Ubisoft
    (publisher), 2008. Nintendo Wii game.

40. Bozon, Mark. No More Heroes Review---IGN. Video Games, Wikis,
    Cheats, Walkthroughs, Reviews, News & Videos---IGN.
    <http://www.ign.com/articles/> 2008/01/22/no-more-heroes-review
    (accessed March 6, 2013).

41. *Nurburgring 1*. Reiner Foerst GmbH (developer and publisher), 1975.
    Arcade game.

42. *Night Driver*. Atari (developer and publisher), 1976. Arcade game.

43. *Wolfenstein 3D*. id Software (developer), Apogee Software
    (publisher), 1992. PC game.

44. *Zaxxon*. Sega (developer and publisher), 1982. Arcade game.

45. *Q\*Bert*. Gottlieb (developer and publisher), 1982. Arcade game.

46. *The Nightmare Over Innsmouth*. Chris Totten (developer), 2011.
    Unreleased PC game.

47. *Resident Evil*. Capcom (developer and publisher), 1996. Sony
    Playstation game.

48. *Killer 7*. Grasshopper Manufacture (developer), Capcom
    (publisher), 2005. Nintendo Gamecube game.

49. *The Prince of Persia: Sands of Time*. Ubisoft Montreal (developer),
    Ubisoft (publisher), 2003. Nintendo Gamecube game.

50. *Portal*. Valve Corporation (developer and publisher), 2007. PC
    game.

51. Alfred Hitchcock on Mastering Cinematic Tension. YouTube.
    [http://www.](http://www/) youtube.com/watch?v=DPFsuc_M_3E (accessed
    March 7, 2013).

52. *Metroid Fusion*. Nintendo R&D1 (developer), Nintendo
    (publisher), 2002. Game Boy Advance game.

53. *Shantae: Risky's Revenge*. Tim and Chris Stamper (developers),
    Ultimate Play The Game (publisher), 1984. Sinclair ZX Spectrum game.

54. *Knight Lore*. Way Forward Technologies (developer and
    publisher), 2010. Nintendo DSiWare game.

55. *Starcraft*. Blizzard Entertainment (developer and publisher), 1998.
    PC game.

56. Lyndon, Donlyn, and Charles Willard Moore. *Chambers for a Memory
    Palace*. Cambridge, MA: MIT Press, 1994, p. 164.

57. Weise, Matthew. The Rules of Horror: Procedural Adaptation in *Clock
    Tower, Resident Evil*, and *Dead Rising*. In Perron, Bernard.
    *Horror Video Games: Essays on the Fusion of Fear and Play*.
    Jefferson, NC: McFarland & Co., 2009,

> pp. 238--266.

58. *Night of the Living Dead*. Film. Directed by George A. Romero.
    Pittsburgh, PA: The Walter Reade Organization, 1968.

59. Michael, Evans. An Illustrated Fragment of Peraldus's Summa of Vice:
    Harleian MS 3244. *Journal of the Warburg and Courtauld Institutes*
    45 (1982): 14--68. <http://www.jstor.org/stable/750966> (accessed
    February 26, 2013).

