# Tools and Techniques for Level Design

> Chapter 2
>
> In the introduction, we gave the working definition of level design as
> "the thoughtful execution of game*play* into game*space* for players
>
> to dwell in." As we move from discussing historic precedents from both
> architecture and game design, we will explore the methods we will use
> to design game levels according to this definition. In this chapter,
> we discuss what game levels do to create user experiences and some of
> the techniques and tools used to create game levels. We also take
> engine-specific work- flows into account to show how you can build
> your own levels in game engines that are available at no cost.
>
> What you will learn in this chapter:
>
> Level design goals for creating game experiences Non-digital level
> design tools
>
> Digital level design tools Level design workflows
>
> Engine-specific methodologies

## LEVEL DESIGN GOALS FOR CREATING GAME EXPERIENCES

> There is something about the act of creating that stirs excitement.
> This is what many people who aspire to be architects and game
> designers seek--- fulfillment in the act of creation. A sure way to
> excite a group of novice
>
> **41**
>
> game designers is to let them create things in a level editor. Much
> less tech- nological but still very powerful is the act of
> drawing---putting the cre- ations of one's mind on paper. Done for the
> sheer act of creation, making game levels in these ways is
> exhilarating.
>
> However, levels made blindly in level editors or on paper are often
> shal- low exercises, based on "wouldn't it be cool" design ideas. In
> the same way an architect should never begin pouring a foundation
> without doing a site, budget, or load analysis, game designers should
> never begin work without taking a very important component of games
> into account---players. Great or even simply good levels should be
> planned---not only to get an image of what the level will look like,
> but also to understand the kind of experience the designer hopes to
> create for players. Therefore, before exploring the different tools of
> level design later in this chapter, it is important to know that game
> levels are the primary tool of communication between game makers and
> game players.
>
> If game levels are interpretations of *gameplay*, that is, the
> constructed system of rules that create a user experience in a game,
> then they are also the medium by which game designers transmit the
> gameplay they've designed. It is important to know this, because so
> often novices in level design open a game's level editor and simply
> begin placing objects in a scene like a child with a new box of LEGOs.
> To be honest, playing with LEGOs is possibly the best analogy for
> creating game levels for reasons that we will explore later. However,
> planning your levels with user experi- ences in mind is the difference
> between building a masterpiece and having a disorganized mess, even if
> it is a pretty mess.
>
> As the primary tool for communication between game designers and game
> players, game levels should be built with three goals in mind. By
> reaching these goals, designers can better direct players through
> games and create meaningful user experiences:
>
> Adjustment of behavior Transmission of meaning Augmentation of space
>
> Concepts contributing to these goals form the content for much of the
> rest of this book. When reached by designers to create game levels,
> gamespaces with powerful communicative properties are created. Such
> gamespaces can deeply affect players, though they should also allow
>
> players to create their own interactions with the game system. Before
> moving forward, let us briefly explore the following goals of level
> design.
>
> Adjustment of Behavior
>
> Many designers argue that a level's primary function is to teach
> players how to play a game. In *Indie Game: The Movie*, for example,
> *Super Meat Boy* artist and designer Edmund McMillen highlights how
> the first sev- eral levels of the game teach players how to play.1 He
> argues that through obstacles that require players to utilize Meat
> Boy's different abilities to pass, players will not only learn Meat
> Boy's different properties, but also gain a sense of accomplishment
> for figuring out how to play. Repetition of these situations, he
> argues, both reinforces gameplay lessons so they are retained and
> teaches players how to combine abilities, such as running and jumping,
> into new moves (Figures 2.1--2.4).
>
> Kremers argues a similar point in his book *Level Design: Concept,
> Theory, and Practice*, with the concept of *skill gates*.2 Skill gates
> are required challenges that block a player's progress unless he or
> she performs a spe- cific action to pass. Such obstacles can be very
> simple, such as an enemy or object that players must jump over (Figure
> 2.5), or more complex, such as games that require you to use new
> abilities to escape from the room where you acquire them (Figure 2.6).
>
> While behavior adjustment can be accomplished in these very planned
> ways, there are also games that allow their players to act in very
> unplanned ways. One celebrated (and sometimes demonized) aspect of
> games is their allowance of taboo behaviors and role-playing. If a
> game allows players the choice of many things to do, especially in
> massively multiplayer online games, they will take on roles that are
> not always necessarily heroic.

![](./media/media/image88.jpeg){width="3.001943350831146in"
height="1.6733333333333333in"}

> FIGURE 2.1 The first level of *Super Meat Boy* requires players to
> jump to save Bandage Girl.
>
> ![](./media/media/image89.jpeg){width="2.099842519685039in"
> height="2.6in"}
>
> FIGURE 2.2 The second level requires the player to use Meat Boy's wall
> jumping ability.

![](./media/media/image90.jpeg){width="2.6937642169728786in"
height="1.02in"}

> FIGURE 2.3 The third level requires players to combine running and
> jumping into a long jump.

![](./media/media/image91.jpeg){width="2.6999464129483814in"
height="2.1199989063867015in"}

> FIGURE 2.4 The final level demonstrates saws to the player in a
> non-interactive fashion before they become obstacles in future levels.
>
> ![](./media/media/image92.jpeg){width="3.008432852143482in"
> height="1.2733333333333334in"}
>
> FIGURE 2.5 An early skill gate in *Super Mario Bros.* requires you to
> jump over or onto an enemy Goomba to pass. This teaches the player to
> jump.

![](./media/media/image93.jpeg){width="2.72125in" height="1.76625in"}

> FIGURE 2.6 After getting new powers in *Metroid* games, players must
> often solve a puzzle related to the new power to escape the item room.
>
> Again, gamespaces can help facilitate this kind of role-play by
> providing environments that mix and match both heroic and support
> characters while providing mischievous players opportunities to wreck
> havoc.
>
> Architecture supports both of these types of gameplay. In different
> cultures and throughout history, architects and builders have used
> spatial configurations to channel occupant activity. Throughout this
> book, we discuss the psychological methods that both games and
> buildings use to adjust user behavior.
>
> Transmission of Meaning
>
> There is an ongoing debate in the game industry between those who
> believe that games should be understood according to gameplay mechan-
> ics, known as ludologists, and those who believe games should be
> under- stood as a narrative medium, known as narratologists. Over
> time, these two factions have settled their differences, and games are
> now often understood for how they utilize both rule-based systems and
> meaningful
>
> structures together. Through explorations of this combination, new
> genres of games have emerged, such as persuasive games. These games
> communi- cate a message or teach players something through gameplay.
>
> Embedding meaning in structural systems is a hallmark of architectural
> design. Much of architectural history is focused around sacred
> structures. Built for occupants who were often illiterate, pictorial
> representations of biblical scenes or figures of deities helped
> communicate the idea of what the structure was supposed to represent.
> Some structures, such as Gothic churches, were built in ways meant to
> simulate the architect's idea of spiri- tual places such as the
> kingdom of heaven.
>
> In games, narrative descriptors contained within a game's dialog, art,
> and symbolism interact with formal and structural elements of game
> levels---rules of movement and the construction of the gamespace.
> Understanding how these work together helps us discern how to create
> meaningful game levels. Rather than simply turning to cutscenes as
> sim- ple story solutions, designers can make their game levels do a
> lot of narra- tive legwork for them. This turns game levels into
> systems of *rhetoric*, the art of communicating ideas through
> discourse. Game theorist Ian Bogost argues that while writing and
> debate are classical forms of rhetoric, and while art and graphics
> make arguments through *visual rhetoric*, games and interactive media
> can make statements through *procedural rhetoric*.3 In Bogost's model,
> games make their arguments through the cause-and- effect relationships
> between player actions and game rules. This is explored later to show
> how gamespaces can help encapsulate narrative or meaning- ful ideas.
>
> Augmentation of Space
>
> Tied in with the idea of transmitting meaning is the concept of
> augment- ing space with information. In video games, user interfaces
> and on-screen icons connect players to databases of in-game
> information (amount of ammo, enemy information, etc.). In some games,
> levels can give informa- tion to players in ways that allow them to
> make informed decisions about what is coming next. Lighted signs in
> Valve Corporation's *Portal* tell play- ers what mechanics a given
> puzzle will involve at the entrance to every chamber. Patterns in
> level design can inform players when bosses or other significant
> enemies are coming (Figure 2.7).
>
> These types of patterned spaces can be powerful ways to commu- nicate
> with players. In architecture, formal *symbols* are often used to
> communicate the function of a building (Figure 2.8). Establishing a
> set
>
> ![](./media/media/image94.jpeg){width="3.9924989063867016in"
> height="1.6425in"}
>
> FIGURE 2.7 Games in the *Mega Man* series typically use a double set
> of gates and a hallway to mark the entrance to a boss room. This
> pattern trains players to know they are about to fight a boss and
> builds anticipation for the encounter by slightly delaying it. Knowing
> that a boss fight is about to happen also allows players time to
> arrange their resources for the battle.

![](./media/media/image95.jpeg){width="3.005719597550306in"
height="2.8533333333333335in"}

> FIGURE 2.8 Look at these building sketches. What types of buildings do
> you suppose they are? Symbolic forms like these help demonstrate to
> observers what the purpose of a structure is without the need for
> signage or verbal indicators.
>
> of formal or spatial symbols allows players to understand what's next
> in a level, or even what objects are interactive (Figure 2.9). Through
> this type of formal interaction, gamespaces build their own formal
> lan- guages that can assist in the augmentation of behavior or
> transmission of meaning.
>
> ![](./media/media/image96.jpeg){width="2.666246719160105in"
> height="1.88in"}
>
> FIGURE 2.9 In many games, interactive objects such as buttons,
> grappling hooks, switches, and others follow similar visual language
> throughout so players know when to use their abilities. The game
> *Mirror's Edge* uses an interesting approach of color-coding
> interactive objects in the otherwise whitewashed world.
>
> New to game development are mobile technologies that allow for
> information to be transmitted not only in the game, but also within
> the real world. Smartphones now support applications for *augmented
> reality* (AR), technology that overlays digital information on the
> real world. With AR-capable devices, game worlds can expand to include
> real-world envi- ronments. Like creating symbols in digital
> environments, AR apps are often programmed to recognize certain images
> in real space and then pair digital information with them. This can
> help players establish a lexicon of forms that have extra meaning in
> the context of the AR app.
>
> So, what kinds of spaces should be augmented with AR to create mean-
> ingful game situations? Is it enough to put a digital layer on any
> real-world environment, or are there ways to plan interesting
> interactions through spatial awareness? Theories of urbanism may hold
> the key to understand- ing how functions of AR, alternate reality
> games (ARGs), and big games (large-scale physical games played in real
> environments) can meaning- fully communicate serious ideas to players.

## NON-DIGITAL LEVEL DESIGN TOOLS

> Now that we've established some of the goals of level design, we can
> dis- cuss some of its tools. Like many things in the game industry,
> there is no one perfect tool for level design. There are many
> available game engines out there, a few of which are listed in this
> book's introduction, that you can use to create your own games. In
> many ways this makes games much
>
> more of an open medium, as games can be made with many tools, even
> non-digital media. However, it can also make breaking in confusing for
> anyone looking for one set path to game development.
>
> Due to the non-standard state of game production, an appropriate list
> of level design tools should be derived from the methodology you
> choose to adopt as a designer. Since in the context of this book, we
> are looking at architecture for inspiration, let us consider some of
> its tools and methods as a starting point for level design
> methodologies---beginning as architects do with basic drawings and
> working toward realized interactive space.
>
> When designing levels, especially 3D ones, designers should strive to
> prototype their levels in interactive form as soon as possible.
> However, one should not underestimate the value of non-digital tools
> for level design. While they do not get designers onto the computer
> and generating work right away, non-digital sketches and maps can be
> of great value.
>
> To be clear, this section is not focused on non-digital drawings as
> the kinds of perspective drawings that are typically used for concept
> art, though those certainly play a part in planning. Instead, this
> type of drawing utilizes architectural diagramming and drawing for
> several different pur- poses. Planning levels on paper is an obvious
> application, allowing design- ers to quickly sketch their ideas before
> working on a computer. However, as we will see, architectural
> sketching can also be useful for recording one's experiences in and
> understanding levels from our favorite games.
>
> Basic Drawing Techniques
>
> University of Washington Professor Emeritus Francis Ching said that
> drawing both "invigorates seeing"4 and "stimulates the imagination."5
> Drawing is a core component of not only architectural work, but also
> visual understanding of designed spaces. It is therefore vital to
> under- stand the basics of architectural design drawing. While one
> might assume that good drawing for artwork is similar to that for
> architectural analysis, there are quite a few differences.
>
> In architectural drawing, you are trying to capture the *shapes*, the
> two- dimensional boundaries of objects; *forms*, three-dimensional
> masses of objects; and *relationships*, how each object interfaces
> with one another in space. Perhaps the biggest difference is that
> architectural drawing is often meant to be more communicative than
> regular sketching, describing to others the forms, shapes, and
> relationships of spaces, and therefore must be neater and more
> precise---free of chicken scratch, hurried shapes, and timid lines
> (Figure 2.10).
>
> ![](./media/media/image97.jpeg){width="3.0034919072615924in"
> height="0.65625in"}
>
> FIGURE 2.10 These are examples of how not to draw lines or shapes in
> architec- tural sketches. Chicken scratch lines and hurried shapes can
> distract from the meaning of a drawing.

![](./media/media/image98.jpeg){width="2.9960378390201226in"
height="0.5906244531933509in"}

> FIGURE 2.11 These line sketches show several different techniques,
> including adding a start and end to each of your lines, how these are
> used to neatly intersect lines, and how squiggled lines create
> directionally straight sketch lines.
>
> *How to Draw a Line*
>
> Creating cleaner, more confident lines is easier than one might think.
> Two techniques can help in drawing clean, straight lines. One is
> beginning and ending each line with a dot or dash. These dots and
> dashes should over- shoot where the line actually ends, so lines
> coming to a corner should intersect slightly. Another technique is to
> squiggle your lines as you draw them. This will provide straighter
> lines. While this seems counterintuitive, wiggling your pen slightly
> while you draw a straight line will cause you to concentrate more on
> the squiggle and less on making your line perfectly straight; the
> result is a line that is more directionally straight (Figure 2.11).
>
> When creating shapes that are not linear, such as circles, it is
> useful to create straight *reference* lines and measure out the shape
> rather than simply attempt to draw it correctly. To draw a circle,
> first draw a square. Then, draw lines through the square horizontally
> and vertically. Now, draw arcs between each midline so that you end up
> with a circular shape (Figure 2.12). When drawing in perspective,
> circles become ellipses, so draw these by either using the sides of an
> object as endpoints for the ellipse or measuring the ellipse out with
> a square drawn in perspective.
>
> *Contours and Line Weights*
>
> The previously mentioned drawings are *contour* drawings. Contour
> draw- ings follow the edges of shapes and forms, describing where
> objects are
>
> ![](./media/media/image99.jpeg){width="2.9170122484689416in"
> height="1.1484372265966754in"}
>
> FIGURE 2.12 To sketch a circle correctly, create a reference square
> and reference lines, and use them as a base to draw a properly
> proportioned circle. Circles in perspective flatten and become more
> elliptical.

![](./media/media/image100.jpeg){width="2.953501749781277in"
height="1.4in"}

> FIGURE 2.13 This contour drawing shows the placement of buildings,
> trees, and other natural features in relation to one another.
>
> in space (Figure 2.13). Contour drawing is what people often start
> with when learning how to draw. Contours also offer a quick way to
> document spatial conditions when in the field.
>
> When sketching in contour and when drafting, *line weights* help com-
> municate object distance. Line weight refers to the thickness or
> darkness of a line used in a drawing (Figure 2.14). When drawing with
> line weights, the thickest weights are assigned to edges that do not
> immediately connect with others, such as the outer contours of an
> object or group of objects. Contours of objects that directly meet
> other objects are given very light line weights.
>
> *Drawing with References*
>
> When sketching designed spaces, reference lines can be used much in
> the same way you would when sketching shapes. If the point of
> sketching is to understand the spatial conditions of the scene you are
> observing, then it is helpful to use light reference lines to line up
> elements of scenery or archi- tectural forms that line up with one
> another in space. Ching also recom- mends using your pencil as a
> *viewfinder* to observe spatial relationships.
>
> ![](./media/media/image101.jpeg){width="3.3395133420822396in"
> height="1.58in"}
>
> FIGURE 2.14 This sketch utilizes line weight to communicate the
> distance edges and contours are from one another. The outer contours
> of objects are therefore the thickest lines in the drawing.

![](./media/media/image102.jpeg){width="2.582617016622922in"
height="1.8666655730533683in"}

> FIGURE 2.15 Techniques for using your pencil as a measuring tool and
> view- finder. From these exercises, you can create reference lines
> that help you under- stand the relationships between objects you are
> drawing.
>
> Holding your pencil with your thumb halfway up the shaft allows you to
> measure the image you are seeing. Holding the pencil further down
> toward the eraser allows you to use the shaft of the pencil as a
> *straightedge* to determine angles and relationships between objects
> so you can draw your reference lines6 (Figure 2.15).
>
> *Shading*
>
> Despite the usefulness of contour drawing, you will occasionally want
> to describe the *surface conditions* of forms you are observing or the
> *lighting conditions* of a space. To do this, you will use methods of
> *shading* to describe these conditions. Shading is using your drawing
> tools in such a way that describes light and *tonal*, information
> related to color, values of an object.
>
> ![](./media/media/image103.jpeg){width="2.6718635170603675in"
> height="1.36in"}
>
> FIGURE 2.16 The two described types of
> shading---hatching/crosshatching and scribbling. Three-dimensional
> forms can be described in sketches by capturing tonal values through
> these methods.
>
> There are several different methods for shading. One of the most
> commonly used is *hatching*, where the artist uses a series of
> parallel lines to describe tonal value. When hatching, darker values
> are created by spac- ing lines closely together, while lighter values
> are created by spacing lines farther apart. *Crosshatching* is a
> similar technique to hatching where two sets of lines are crossed over
> one another to create values. Crosshatching and hatching can be used
> interchangeably in the same drawing to create many different tonal and
> textural values.
>
> In his book, Ching describes another useful method, called
> *scribbling*, that has artists putting down more random lines to
> denote tonal value than one would while hatching and crosshatching.
> Scribbling is useful for on-site drawing situations where not a lot of
> time can be devoted to creat- ing neat hatch lines. By keeping
> scribbling methods consistent, artists can still create neat and
> communicative drawings7 (Figure 2.16).
>
> *Hierarchical Drawing*
>
> With all these methods, it is important to remember the purpose of
> your drawings---communication of the spatial conditions of places you
> are observing. In this way, you must remember to create your drawings
> in a *hierarchical* fashion, that is, in such a way that best
> communicates the information you are trying to convey without getting
> caught up in extra- neous details. For example, when trying to sketch
> details on the façade of a Gothic church, it is better to focus on the
> church itself rather than sketch- ing people and landscape elements
> around the church. Such elements can be abstracted with scribbles or
> rough contours.
>
> When trying to establish your visual hierarchy, it is also important
> to draw in such a way that accentuates the most important part of the
> drawing. For example, shading or outright blacking out the unimportant
>
> ![](./media/media/image104.jpeg){width="2.7700339020122486in"
> height="2.506666666666667in"}
>
> FIGURE 2.17 Two versions of the same sketch. One shows the proper way
> to establish visual hierarchy by focusing more attention onto the
> subject of the sketch. The other shows how silhouettes of unimportant
> details can take atten- tion away from the drawing's subject. The
> subject of these sketches is the Martin Luther King Memorial Library
> in Washington, D.C. It was designed by Ludwig Mies van der Rohe and
> completed in 1972.
>
> elements of a drawing can have the adverse effect of seeming
> hierarchically more important. Intricate details or dark values
> capture the eye of a viewer much better than lightly drawn lines, so
> you should focus details and dark tones on the part of a drawing you
> wish to accentuate (Figure 2.17).
>
> Types of Architectural Drawings
>
> Once a designer understands how to best draw for spatial design, he or
> she must learn the types of design drawings used to communicate the
> com- position of a space. Each type is used to show specific
> information about a building design from a specific point of view. The
> types of architectural drawings that we will utilize are:
>
> Plan Section Elevation
>
> Axonometric Perspective
>
> *Plan*
>
> Plans are top-down drawings of a space that show spatial relationships
> between the elements of a design (rooms, hallways, stairs, gardens,
> lawns, landscaping features, etc.) from above (Figure 2.18). Like the
> other con- struction drawing types we will discuss, they are drawn
> without perspec- tive. They are drawn assuming that the viewer is
> observing the design from 4½ feet above the ground level. Masses such
> as walls or other objects that pass through this viewing plane (it is
> best to imagine a giant saw blade cut through the space at 4½ feet
> above the ground) are darkened either through hatching or *poche*,
> completely blacking in the contours of the cut form. Hatching in this
> case can be useful for describing material type, a tech- nique common
> in many architectural drawings rendered on the computer. Franco-Swiss
> architect Le Corbusier is famously quoted as saying that "the plan is
> the generator" in his book *Toward an Architecture* (popularly known
> as *Towards a New Architecture*).8 Indeed, plans are typically the
> first drawing that an architect creates when creating building
> designs. Plans show the arrangement and flow of spaces in a design.
> They provide a useful top-down view of spaces that make them suitable
> for diagram- ming (Figure 2.19). When designing levels, many designers
> will draw at least one plan diagram or sketch to visualize how their
> gamespaces will be arranged. Often viewed simply as maps, carefully
> drawn plans can pro- vide meaningful spatial layouts for viewing
> things like level challenges
>
> and pacing, which are covered later in the chapter.

![](./media/media/image105.jpeg){width="3.2054297900262467in"
height="1.8058606736657918in"}

> Coffee shop
>
> plan
>
> FIGURE 2.18 Plans show the flow and relationships between spaces in a
> design. Blacked-in masses show built elements. This plan shows a
> simple coffee shop layout.
>
> ![](./media/media/image106.jpeg){width="2.2909503499562556in"
> height="1.6475in"}Hearth "center of house
>
> Fallingwater public/private diagram
>
> FIGURE 2.19 This drawing shows how plans can be used to diagram
> spatial articulations in a design.
>
> Despite these strengths, the primary downside of plan drawings is
> their lack of three-dimensionality. To describe spatial conditions
> above and below the level shown in a drawing, dotted lines are
> typically used, but to properly capture multilevel spaces, a different
> type of drawing is used.
>
> *Section*
>
> In terms of technique, building sections are very similar to plans, as
> they depict a design cut along a plane. However, rather than the
> design being cut horizontally to show a top-down view, sections show
> views into the building as though they had been cut through vertically
> (Figure 2.20). Like plans, cut-through masses are colored in with
> poche. Most sections show the *elevation*, perspective-less drawings
> of the side of an object, of forms and objects past the cut line,
> though sectional perspectives and other combinations are quite common.
>
> Sections are often used in tandem with plan drawings to describe
> three- dimensional space. According to architectural writer Matthew
> Frederick, "Good designers work back and forth between plans and
> sections, allow- ing each to inform the other."9 Sections can help a
> level designer map out vertical spatial arrangements for things like
> multilevel puzzles or battle positions in multiplayer maps. As many 2D
> games are viewed from the side, sections can offer the same overview
> of side-scrolling game levels for better planning of level pacing.
>
> Plans are especially important for 3D titles. If you design in a
> two-dimensional plan, your game level will be two-dimensional, even in
>
> ![](./media/media/image107.jpeg){width="3.0187325021872264in"
> height="1.8199989063867017in"}
>
> FIGURE 2.20 A building section of Fallingwater by Frank Lloyd Wright.
> It was built between 1936 and 1939 in Mill Run, Pennsylvania.
>
> a 3D game. Having several sections of the major play spaces in your
> levels will allow you to visualize alternate ways of transitioning
> from play space to play space. Sections allow you to better utilize
> height-based spatial tran- sitions such as ramps, overhead bridges,
> cliffs to jump down, and similar structures that are difficult to
> encompass in a plan drawing.
>
> *Elevation*
>
> Elevations are the third type of architectural drawing. Elevations are
> sim- ilar to sections, but instead of cutting through a design, the
> viewpoint is from the outside of the building. Elevations are used to
> show exterior views of a building's sides (Figure 2.21).
>
> Architects use elevations primarily to visualize the exteriors of
> build- ings. For real buildings, this is vital. However, game levels
> often lack the need for real building conditions like having both an
> exterior and an inte- rior. Instead, the designer will only create
> those surfaces that the player will look at. Even so, elevations are
> still important for designing good building exteriors for scenery.
> Elevations in level design fall more under the category of concept art
> rather than spatial planning.
>
> *Axonometric*
>
> When planning 3D video games, plans and sections must work together to
> correctly show 3D space. However, *axonometric* drawings can be used
> to represent a design's three-dimensionality. To create an axonometric
> (axon) drawing, artists take an already-made plan drawing and turn it
> either 30 or 45 degrees, and then project the plan upward to create 3D
> forms of the design (Figure 2.22).
>
> ![](./media/media/image108.jpeg){width="3.769978127734033in"
> height="1.6333333333333333in"}
>
> FIGURE 2.21 A building elevation of Villa Savoye by Le Corbusier. It
> was com- pleted in 1931 in Poissy, Yvelines, France.

![](./media/media/image109.jpeg){width="2.4747681539807522in"
height="4.179998906386702in"}

> FIGURE 2.22 An axonometric drawing. This one is a *sectional
> axonometric*, showing the extruded interior geometry of the design and
> the plan that forms the base of the drawing.
>
> Axonometrics are powerful spatial planning tools. They often combine
> plan and elevation drawings, and can even combine plan and section to
> create *sectional axonometric* drawings like the one seen in Figure
> 2.22. As drawings that are derived from others, creating axonometrics
> is often a question of time for level designers. On one hand, they can
> help visualize 3D space. On the other, they take extra time to produce
> what could be used for creating level prototypes in your game engine.
>
> Level designers that use axonometric drawings tend to create
> semi-planned axonometrics. They show the three-dimensionality of a
> gamespace but may or may not fully follow a plan of the level. These
> can be done for several different purposes. One potential purpose is
> to cre- ate spatially planned concept art for a game level space,
> combining plan and elevation to communicate what the final level
> geometry may look like. Valve, on the other hand, has used
> axonometric-like drawings of levels to demonstrate three-dimensional
> gameplay concepts.10 These axons create the level space only as a
> visual guide rather than a plan of the actual level. Instead, they use
> this visual guide as a backdrop for sketches of gameplay events that
> will happen in the level in a three-dimensional way---allowing for the
> mapping of vantage points, sniping spots, or spatial puzzles. In this
> way, axons become both concept art and a game design tool (Figure
> 2.23).

![](./media/media/image110.jpeg){width="3.9706802274715662in"
height="2.953333333333333in"}

> FIGURE 2.23 These axonometric drawings diagram a level with added
> notes for gameplay situations.
>
> *Perspective*
>
> Finally, there are *perspective* drawings. Like axons, perspective
> drawings show 3D space. However, unlike axons, which are drawn without
> distor- tion, perspective drawings show how an object distorts based
> on the view- er's positioning relative to a *vanishing point* (Figure
> 2.24).
>
> Perspective drawings can be drawn with multiple vanishing points.
> Drawings based on one vanishing point, where one side of an object is
> drawn without distortion in an elevation style, is called a *one-point
> per- spective*. Drawings that utilize two vanishing points to distort
> more than one side of an object are called *two-point perspectives*.
> Two-point per- spectives are the views most commonly seen from a
> human's eye level. Drawings using three vanishing points, most often
> done for views of tall buildings from above or below, are *three-point
> perspectives*.

![](./media/media/image111.jpeg){width="2.848596894138233in"
height="4.084763779527559in"}

> FIGURE 2.24 Diagrams of perspective drawing, showing how objects are
> drawn to distort toward one or more vanishing points. These diagrams
> show one-, two-, and three-point perspectives.
>
> Perspectives are most often used for concept art, as they are the
> least useful for actual spatial planning but most useful to develop
> the visual art of a level. They can either be drawn manually or
> generated through *3D underlays*. Three-dimensional underlaying is
> when an artist creates a simple version of his or her concept art
> scene in a 3D art program, then paints on top of it using a digital
> art program like Photoshop. Such under- lays are helpful for creating
> many versions of the same scene to develop a game's final art style
> (Figure 2.25).
>
> Now that you know a few different drawing techniques and the types of
> drawings used to understand spatial design, we will show how these
> tech- niques can be applied to better understand and plan game levels.

![](./media/media/image112.jpeg){width="2.5053313648293964in"
height="2.1599989063867016in"}![](./media/media/image113.png){width="2.8585137795275593in"
height="0.4696106736657918in"}![](./media/media/image114.jpeg){width="0.4765551181102362in"
height="0.9383606736657918in"}![](./media/media/image115.png){width="2.8585137795275593in"
height="0.4704713473315836in"}![](./media/media/image116.png){width="2.8585137795275593in"
height="0.4713462379702537in"}![](./media/media/image117.jpeg){width="0.4765551181102362in"
height="0.9383606736657918in"}![](./media/media/image118.png){width="2.8585137795275593in"
height="0.46875in"}

> FIGURE 2.25 This perspective sketch of a building was painted over a
> simple 3D rendering. Such underlays can be used to create multiple
> looks for the same model.
>
> Sketching and Journal Writing
>
> Design drawing is vital for visual understanding of designed spaces.
> The drawing techniques covered in the two previous sections can be
> applied both for spatial design drawings in 2D and for recording
> observa- tions and ideas. For the architect, sketching is an important
> way to both capture design ideas and record elements he or she has
> seen while study- ing a piece of architecture (Figure 2.26). Sketching
> can also be vital for communicating those design ideas later.
>
> In Chapter 1, we discussed a way of seeing for game levels and
> buildings. The guidelines for seeing include things like understanding
> why the level is created the way it is, what gameplay experiences it
> creates, what its histori- cal precedents are, and what its spatial
> composition is. Early in an archi- tect's education, he or she is
> taught to record these kinds of observations in sketchbooks. Using the
> level design ways of seeing that were isolated in the previous chapter
> as a guideline, we can also do similar studies for game lev- els.
> Having such a sketchbook can be vital for understanding design prec-
> edents that will be inspirations for your own levels (Figure 2.27).

![](./media/media/image119.jpeg){width="2.2598304899387576in"
height="3.153332239720035in"}

> FIGURE 2.26 Sketches such as these are important tools for both
> aspiring and pro- fessional architects for understanding buildings.
> Sketching allows the architect to both highlight elements he or she
> finds important in the design and gain a greater understanding of the
> building by recreating its forms through manual drawing.
>
> ![](./media/media/image120.jpeg){width="2.50125in"
> height="3.4763746719160107in"}
>
> FIGURE 2.27 Here are some sketches of *Half-Life 2* environments
> derived from gameplay journals recorded during gameplay sessions.
> Writing down how you feel during gameplay sessions and taking
> screenshots can help designers mark what they will analyze with
> sketches like these later on.
>
> Granted, for many games, one cannot sketch and analyze while being
> attacked by waves of enemies. In many cases, keeping a gameplay jour-
> nal and sketchbook concurrently can help players retain their memories
> of gameplay. On computers, taking screenshots or videos during game-
> play and adding them to your journal is also an excellent way for
> marking what to analyze later on. After taking appropriate screenshots
> and mak- ing notations about what occurs in certain sections of a
> game, analysis sketches can be derived from these digital recordings.
>
> Designing on Paper
>
> Beyond recording precedent analyses, sketching is useful in level
> design for quickly recording design ideas. In architectural design,
> initial ideas are often sketched out in sketchbooks or on trace paper.
> A standard way of forming design ideas on paper is to do *parti*
> sketches. An archi- tectural parti is a simple formal study that seeks
> to isolate the shape a building will eventually take. These studies
> can be done on paper or as
>
> architectural models, in both two and three dimensions. For buildings,
> these are important for understanding the formal principles that will
> gov- ern a design and how a building will interact with its *site*,
> the place where it is built (Figure 2.28). Perhaps as importantly,
> parti studies are noncom- mittal, meaning that a designer can quickly
> create a large number of them without having to commit a lot of effort
> and detail into any one design, only to realize it was the wrong
> choice later. They also lack measurement in most cases, so designers
> can focus more on spatial and formal ideas rather than sizing. Parti
> is explored later in the chapter as an element of level design
> workflows.
>
> For more measured level design drawing, a useful tool for generating
> paper level ideas is *graph paper*. Graph paper is commonly used to
> plot various mathematical functions---thus the name. It comes in many
> types, but the type most commonly used by building engineers is
> *Cartesian graph paper*, which features a regular grid. While not
> always used by architects, engineers use graph paper as an aid when
> drafting tools like rulers and triangles are not handy. It is
> especially useful for figuring out the propor- tions of objects in a
> sketch. To do this, builders stipulate that one square

![](./media/media/image121.jpeg){width="2.897285651793526in"
height="3.066666666666667in"}

> FIGURE 2.28 Architectural parti sketches allow designers to quickly
> under- stand how their design will interact with site conditions. They
> also help designers try different spatial and formal compositions
> quickly without having to commit to any one design.
>
> on the paper represents a specific unit of measurement (1 square = 1
> yard, for example), and use that as a base for generating quick but
> accurately measured sketches.
>
> Spatial design for games also has a close relationship with graph
> paper. It is the primary tool of many who have created their own maps
> for the role-playing game *Dungeons and Dragons*. However, for video
> games, where the designer will eventually implement his or her design
> on a computer with a character that will appear to physically interact
> with the game world, creating architect-like graph paper drawings will
> help the designer figure out proper proportions for game worlds. A
> common mistake new designers make is to generate game levels on the
> computer that do not appropriately fit around a player character. In
> some extreme cases, this can mean that the player character cannot
> even go through doors.
>
> To properly design levels, a level designer must understand a player
> character's *metrics*. Metrics are gameplay-based measurements
> expressed in in-engine units that describe size and movement
> properties of charac- ters in games. Measurements that could be
> considered metrics include the size of the character, the space
> traversed by jumps, the space taken up by attacks, the distance
> traveled over time when the character runs or walks, and many other
> movement-based things. Many game engines employ their own basic units
> of measurement; one unit in the Unity game engine, for example, equals
> 1 meter, which can allow designers to understand the distance player
> characters use to do things.
>
> Graph paper can serve similar purposes before the design is created on
> the computer. By stipulating that a square or group of squares on
> graph paper is equal to a specific unit of measurement, level
> designers can plan their levels according to player metrics similarly
> to how architects design according to specific units of measurement
> (Figure 2.29).
>
> Now that you understand some of the possibilities for recording your
> experiences with existing levels and planning your own through non-
> digital means, we can move on to discussing how digital tools can help
> extend our planning process and bring them into implementation in game
> engines.

## DIGITAL LEVEL DESIGN TOOLS

> The goal of a level designer should be to get his or her designs in
> interac- tive form as soon as possible. This way, he and others can
> *playtest* the level design, meaning that he plays the game to
> evaluate whether it fulfills its
>
> ![](./media/media/image122.jpeg){width="2.6702515310586175in"
> height="3.6066666666666665in"}
>
> FIGURE 2.29 This design sketch, showing the plan of a level, utilizes
> graph paper to help the designer match gamespace measurements against
> the size of the player character in a 3D game.
>
> original design goals. Once a designer has taken the time to plan
> levels on paper, concretely forming a plan for how the level
> experience will play out, he can begin to digitize his ideas.
>
> Digital tools for level design can fulfill a great many functions, in
> both level generation and planning. One might wonder why additional
> plan- ning may be needed after spending considerable time doing
> architectural sketches of levels on paper. However, as we will see,
> digital tools can help plan spatial conditions that will be discussed
> in greater detail later in the book, such as the materials of
> different surfaces and lighting conditions, and can offer ways to plan
> out the measurements of environmental objects during the drawing
> phase.
>
> Like the last section, this is not a prescriptive list, but rather a
> list of tools, what they are used for in terms of architectural
> drawing, and how they can help the process of level design. Again,
> your choice of tools should be based on your own process or the
> process that is most appropriate for your own games.
>
> CAD Programs
>
> Although this book does not give level designers tutorials on
> computer- aided design (CAD) software, CAD programs can be a useful
> next step for level designers that want their drawings to demonstrate
> more information than a single sketch can. The traditional software
> used by architects is Autodesk's AutoCAD. However, free alternatives
> like Dissault Systemes' DraftSight are also excellent, especially if
> CAD is used only occasionally by a designer (Figure 2.30).
>
> There are several potentially useful applications of CAD software for
> level designers. The most obvious is that digital drawings have great
> advantages in clarity over hand drawings, as shown in Figure 2.31.
> Clear drawings can convey information much better than rough ones.
> When drafting, CAD programs can make the contents of a sketch clearer
> in a shorter amount of

![](./media/media/image123.jpeg){width="2.7026804461942255in"
height="2.16963801399825in"}![](./media/media/image124.jpeg){width="1.8026935695538058in"
height="2.5982217847769027in"}![](./media/media/image125.jpeg){width="2.7026804461942255in"
height="0.4339304461942257in"}

> FIGURE 2.30 DraftSight provides everything a level designer would need
> from a CAD program.

![](./media/media/image126.png){width="2.5in"
height="0.4838746719160105in"}![](./media/media/image127.png){width="2.5in"
height="0.4838746719160105in"}

> FIGURE 2.31 This simple CAD plan of a level shows the clarity at which
> level maps can be created.
>
> time than hand drafting can. Additionally, CAD programs have features
> that force designers to work in logical ways that translate well into
> game engines. One such feature of many CAD programs is *snapping*,
> where the draw- ing cursor locks, or snaps, to a point in space when
> within a certain radius. Like graph paper, CAD drawings can be set up
> on a grid of dots that can be set as snapping points for the drawing
> cursor. Another useful part of this system is that the grid spacing
> can be set to real-world units. Designers working with game engines
> that have specific unit measurements, such as Unity or Source, can
> greatly benefit from grids and snaps. With these features activated,
> designers can draw in regimented ways that are similar to the logic of
> game engines---working out measurement problems in the drawing phase.
> Beyond the workspace advantages, CAD programs also allow drawn lines
> and shapes to be copied, stored, and modified in various ways so that
> designers can edit quickly without redrawing things
>
> by hand (Figure 2.32).
>
> Another useful feature of CAD software that is applicable through- out
> the entire level design process is *modular design*. In both
> professional architecture and level design, many designs are created
> out of prefabri- cated pieces that are ordered from a manufacturer and
> installed. In archi- tecture, many components of buildings come
> prefabricated: plumbing fixtures, windows, doors, structural elements,
> curtain wall systems, etc.

![](./media/media/image128.png){width="3.338508311461067in"
height="2.5156244531933507in"}

> FIGURE 2.32 This image shows just a few drawing modifications that are
> stan- dard to many CAD programs. Pictured are lines and shapes that
> have been offset, filleted, hatched, and arrayed.
>
> Modular design will be explored in more detail later in this chapter,
> but with CAD software, a standard practice is to store components that
> will be used many times, such as doors or plumbing fixtures, as
> *blocks*. Blocks are drawings that are stored as a separate document
> so they can be inserted and scaled in future drawings (Figure 2.33).
>
> Where this applies to level design is in the discovery of what pieces
> of a level will be utilized multiple times. If designers use CAD
> software or graph paper to sketch out their levels and find themselves
> using a certain wall shape or environmental object multiple times,
> they can decide that the object should be prefabricated for repeated
> use. When levels go into production and 2D and 3D art is being made,
> the designer can have a list of what objects he will need to complete
> his design that he can use or give to environment artists. This kind
> of preproduction planning of levels allows for a LEGO-like
> construction method for levels rather than having to custom build each
> environment.
>
> A final useful application of CAD software in level design is as line
> drawings for use in digital art programs. As great as line drawings
> are for planning levels from plan, section, and elevation, they often
> miss the mark in planning atmosphere. This is where rendering your
> drawings can be handy. If a designer is using CAD software, he can
> base his digital paint- ing on a clean drawing that can become a very
> communicative rendering.

![](./media/media/image129.png){width="4.016885389326334in"
height="2.6266666666666665in"}

> FIGURE 2.33 This toilet image has been stored as a block and can be
> inserted into drawings as the designer likes.
>
> Digital Art Programs
>
> Rendering is the process by which a designer enhances a drawing with
> color and lighting information through artistic media. In this way,
> using digital art programs like Adobe Photoshop or the GNU Image
> Manipulation Program (GIMP) to do the same to level design drawings
> merges architec- tural level design preproduction and traditional
> concept art.
>
> Like more traditional concept art, rendered plans can be used to con-
> vey the atmosphere of game levels in ways that concept perspectives
> can- not. While concept perspectives are excellent at conveying the
> general atmosphere of a level, they cannot properly convey changes in
> atmosphere unless additional design perspectives are done. With an
> architectural drawing of a level, designers can show the progression
> of a level's atmo- spheric effects or materials with a single drawing
> (Figure 2.34). Macro views like those provided in plan drawings allow
> designers to visualize *the atmospheric progression* of their levels
> over time.
>
> When using these types of programs, it is wise to understand their
> most powerful feature: *layers*. Starting with Photoshop, digital art
> programs have allowed users to divide their images into separate
> layers that can each have their own special effects or adjustments
> applied (Figure 2.35). Like in most other pieces of concept art,
> layers are useful both for adding effects to an image and controlling
> what information is visible. For example, having notes on their own
> separate layer allows written information like that in Figure 2.34 to
> show for design discussions or be hidden for clean displays of the
> art.

![](./media/media/image130.png){width="3.8in"
height="0.8330129046369203in"}![](./media/media/image131.png){width="3.8in"
height="0.8341666666666666in"}![](./media/media/image132.png){width="3.8in"
height="0.416499343832021in"}

> FIGURE 2.34 This rendered version of the CAD map from Figure 2.31 dem-
> onstrates how additional information such as textures and lighting can
> be used with digital art programs.
>
> ![](./media/media/image133.jpeg){width="1.3351990376202976in"
> height="2.366665573053368in"}
>
> FIGURE 2.35 The layers window from Adobe Photoshop. Layer effects like
> those applied to the layers in this image can greatly enhance level
> map concepts.
>
> If your game is two-dimensional and a digital art program is where you
> will be creating your final art assets, you can utilize a pixel-based
> measurement system for sizing game objects. For example, if you are
> creating a character that on paper or in CAD is 1 grid square wide by
> 2 grid squares high and jumps at a distance of 8 grid squares horizon-
> tally, you can easily convert these to power of 2 pixel measurements
> supported by most game engines. Using these proportions, you could
> make a character that is 16 pixels wide, 32 pixels tall, and that can
> jump 128 pixels horizontally. You will thus know to proportion any
> level assets and their spacing to these measurements so that the game
> func- tions correctly.
>
> Engine Primitives and Placeholder Art
>
> Whether you are working in 2D and using a digital art program for
> assets or in 3D, where you will need to use a 3D modeling program, you
> should again be focusing on getting your game into interactive form as
> quickly as possible through a game engine. A common mistake many new
> designers make is to assume that gameplay cannot be tested until there
> is art to put into the engine. It is much more efficient, however, to
> design the spaces of a level and create any required *scripts*, pieces
> of code that make game ele- ments work, while art is being developed.
> In this way, a level designer can test whether his or her paper
> designs effectively create the game experi- ence he or she wants.
>
> To do this, game prototypes can be created out of *engine primitives*,
> the simple geometric forms that come with some game engines. In a
> typical engine, this consists of cubes/rectangular solids, spheres,
> cylinders, and planes. Some engines may also include stairs, cones,
> and other shapes (Figure 2.36). Engine primitives can create a
> surprising variety of level geometry, and in fact, many engines' level
> editors are robust enough that most of the larger spatial geometry of
> a level can be created entirely out of primitives. For engines without
> primitives, like many 2D game engines, designers can use *placeholder
> art* (often also called *programmer art*) in the same way. Placeholder
> art typically consists of simple shapes---squares, circles, triangles,
> etc.---that are used to test gameplay until final art is imported.
>
> Primitives can nicely follow the planning done by designers using
> graph paper or CAD drawings, as they are often subject to a standard
> system of measurements dictated by the game engine. An extreme example
> of this is Valve's Hammer level editor, part of the Source engine,
> which requires users to design on a grid with snapping always
> activated. It does this to avoid holes in a level, which will prevent
> the level from compiling into a Source game. Hammer's primitive
> objects automatically snap to measure- ments in the power of 2, so
> objects can have Hammer unit lengths of 16, 32, 64, 128, and so on
> (Figure 2.37). Many 2D engines work with similar power of 2
> measurements, so placeholders should be made at those mea- surements
> in pixels.

![](./media/media/image134.jpeg){width="0.8757053805774279in"
height="2.48in"}

> FIGURE 2.36 The primitive shapes in the Unreal Development Kit (UDK).
>
> ![](./media/media/image135.jpeg){width="4.505374015748031in"
> height="2.433333333333333in"}
>
> FIGURE 2.37 Building with primitives in the Source engine forces users
> to use grid snaps similar to those found in CAD programs.

![](./media/media/image136.jpeg){width="2.2935684601924757in"
height="1.657318460192476in"}![](./media/media/image137.jpeg){width="1.3774442257217847in"
height="2.066180008748906in"}![](./media/media/image138.jpeg){width="2.2935684601924757in"
height="0.41323600174978126in"}

> FIGURE 2.38 This prototype of a zombie FPS was created entirely out of
> Unity engine primitives. Enemies and allies were scripted to create a
> defense sce- nario where players had to hold off a horde as long as
> they could before being overwhelmed.
>
> Another benefit of getting right into primitives is that designers
> will have full access to an engine's systems, such as particles,
> lighting, and others that can influence the look of a game. In this
> way, they can begin to test gameplay scenarios against their
> atmosphere as early as possible. Combined with scripting, designers
> can create rather robust prototypes of their games without the need
> for developed artwork (Figure 2.38).
>
> 3D Modeling Programs
>
> In 3D game engines, environmental objects are designed in 3D modeling
> programs and imported into the engine itself. Like working with 2D
> level assets or level primitives, these 3D assets can be created
> according to measure- ment systems defined during planning stages. The
> degree that you will have to use 3D programs to generate level
> geometry will vary by engine: UDK and Hammer's level editing system
> allows designers to do a lot of work in-engine, while it is best to
> model level geometry for Unity elsewhere. For the engines with rich
> level editing power, the main environmental models that will be
> imported will be decorations or specialty items: furniture, mechanical
> parts, alien architecture, etc. In these cases, scale is less of a
> factor. However, if you are using an engine where most of your level
> geometry, including the actual rooms of a level, must be imported from
> a 3D modeling program, managing scale between the 3D program and
> engine is very important.
>
> Like engines, 3D content programs have their own scales and measure-
> ment systems that designers can build their models to, typically
> defined as a generic unit. If the environment artist translates level
> geometry measure- ments from paper into the 3D program's unit system,
> for example, 1 grid square = 1 unit, then objects can be built to
> proper scale with one another. One simple methodology for bringing
> environmental models from a 3D program into an engine and maintaining
> their scale with one another is to model your entire level in the 3D
> program (Figure 2.39). It can also

![](./media/media/image139.png){width="3.3482010061242344in"
height="2.0066655730533682in"}

> FIGURE 2.39 This jungle level was modeled in its entirety in a 3D
> program and then imported into the game engine as individual
> landmasses. Aesthetic elements like the river that flows through the
> level were modeled to fit around the pieces. This created a system
> that was prescriptive, but that allowed for adjustments to be made
> in-engine without having to go back into the 3D program.
>
> be convenient for building environmental decorations, as they can be
> built and arranged in context with the rest of a level (Figure 2.40).
> This method also offers memory advantages, as some game engines will
> find a single model much easier to render. The problem, however, is
> that you are mod- eling your level in a non-interactive program, so
> testing can be very slow. Proper planning of your unit metrics (the
> character jumps 4 units far, so gaps should accommodate that, etc.)
> can help alleviate this problem, but testing your level layout
> requires awkward exporting and importing. For this, it is better to
> establish a system for dividing your level up into parts in the 3D
> program and assembling it in your engine (Figure 2.41).
>
> Importing 3D models into engines is where managing scale becomes
> difficult. Since each 3D program and engine has its own measurement
> sys- tem, they may not sync up when 3D objects are imported into an
> engine.

![](./media/media/image140.png){width="3.0129035433070865in"
height="1.7933333333333332in"}

> FIGURE 2.40 In this close-up shot of the model from Figure 2.39,
> environment décor can be seen. Each was modeled on the landmass to
> check for proper pro- portion, and then exported individually into the
> game engine where it could be copied and arranged as needed.

![](./media/media/image141.png){width="3.0126465441819774in"
height="1.3266666666666667in"}

> FIGURE 2.41 To create a series of city levels for the game *SWARM!*,
> tiles were created in 3D programs and imported into the engine so a
> few parts could be used to create many level designs.
>
> It is common for objects to import at very big or very small sizes in
> comparison to a scene, so some understanding of the relationship
> between your 3D program's measurements and your engine's measurements
> is in order.
>
> If you are modeling all of your level objects at a standard scale in
> your 3D program, such as the previously mentioned 1 grid square = 1
> unit, then all of your level geometry should import at the same scale.
> If, for example, you find that your objects are importing at 1/20 of
> the size they are supposed to be, you can import each of your
> similarly proportioned objects at twenty times their size. If you
> modeled at the same scale, then each object should import at the same
> scale, requiring you to remember one scale factor.
>
> An alternative to scaling objects when you import them is figuring out
> the proportions between units in your 3D program and units in your
> engine. For example, 1 unit in both Maya and Blender = 1 unit in
> Unity. This is not always necessarily true for 3D Studio Max. However,
> Max can use real-world units, so designers can model in proper scale
> if they utilize the metric system, as 1 Unity unit = 1 meter. Other
> engines have similar proportions. Once they are figured out, you can
> even build a *scaling model* for your 3D program, which is often just
> a box built at the standard scale of a character or unit that is used
> as a "measuring tape" for building level geometry (Figure 2.42).
>
> Now that you understand the digital tools of a level designer and how
> they are implemented in level building, you can use them to generate

![](./media/media/image142.jpeg){width="2.3552077865266843in"
height="1.7133333333333334in"}

> FIGURE 2.42 This screenshot shows some level geometry tiles for the
> side of a building alongside some reference models, shown in a darker
> color. The rectan- gular solid model is scaled to the size of a
> character, while the planar level geom- etry reference models are
> scaled to be 1 unit by 3 units and 3 units by 3 units in the game
> engine. Also pictured is a reference model for a door.
>
> your own game levels. In the next section, we discuss some workflows
> for designing levels and implementing the tools we have discussed.

## LEVEL DESIGN WORKFLOWS

> The American architect Louis Sullivan, often credited as the creator
> of the skyscraper, once famously said, "Form ever follows function."
> This was shortened to the famous design idiom, "Form follows
> function." With this phrase, Sullivan stated one of the driving
> principles of architectural *Modernism*. Modernism was an
> architectural movement of the early twen- tieth century defined by an
> emphasis on creating buildings whose form was derived from their
> purpose. In Modernist architecture, ornament was generally a product
> of the building itself or applied for a purpose, rather than simply
> for the sake of aesthetics. Similarly to Sullivan, Le Corbusier
> stated, "The house is a machine for living in." Much of his
> architecture, as with the architecture of Frank Lloyd Wright, Walter
> Gropius, Louis Sullivan, and others, was focused on purposefully
> creating an experience for the occupants.
>
> As we have seen, the same can be said of level design. In level
> design, developers often design with a specific experiential goal in
> mind. In a 2008 interview, Valve level designer Dario Casali argued
> that "experience is key" when creating level design ideas.11 We have
> previously discussed some goals of level design that related to how
> users use gamespace and how we as designers communicate to the user
> through the space. These experiential goals should dictate how we as
> level designers construct space: form follows function.
>
> In the previous section, we discussed some tools used by level design-
> ers, from drafting ideas on graph paper to using scaling models and
> mea- surement systems in engines and 3D programs. In this section, we
> will discuss some workflow processes that involve these tools,
> beginning with how "form follows function" fits into game design.
>
> Form Follows Core Mechanics
>
> The tenets of form follows function thrive in game design through a
> concept known as the *core mechanic*. A core mechanic is often defined
> as the basic action that a player makes throughout the course of a
> game. In his doctoral dissertation, game designer Aki Jarvinen created
> a core mechanic-centered design method where designers began from
> verbs.12 If one looks at core mechanics as the basic verb of what a
> player does in a game, one can understand the foundational elements of
> what builds each
>
> game's unique experience. For example, *Super Mario Bros.*13 can be
> said to be about jumping, *The Legend of Zelda*14 is about exploring,
> *Katamari Damacy*15 is about rolling, *Angry Birds*16 is about
> flinging, and so on. Beginning from this core, other actions are added
> that define the rules of the final game product.
>
> When designing levels, having a similar core mechanic idea in mind is
> necessary. While many new designers assume that individual levels
> should simply follow the core mechanic of the game, it is possible to
> define level core mechanics to make each unique. An example is the
> Badwater Basin level (Figure 2.43) of Valve's *Team Fortress 2*
> (*TF2*).17 In this level, the game's Builders League United (BLU) team
> must push a bomb into their opponent, the Reliable Excavation
> Demolition (RED), team's base via a mine cart on a track. The mine
> cart mechanic of Payload mode, for which Badwater Basin is a map,
> takes *TF2*'s standard team-based first-person shooter (FPS) mechanics
> and adds a twist. This changes not only the mechanics of gameplay, but
> also the conditions of the level's spatial geometry.
>
> One example cited by Casali, who helped design Badwater Basin, was the
> level's tunnel. In the first prototypes of the level, designers made
> the

![](./media/media/image143.jpeg){width="3.3337489063867016in"
height="2.792583114610674in"}

> FIGURE 2.43 A plan diagram of Badwater Basin from *Team Fortress 2*.
> RED and BLU team bases are marked on the map, as are major circulation
> areas and BLU checkpoints between the two bases.
>
> ![](./media/media/image144.jpeg){width="2.503607830271216in"
> height="2.38in"}
>
> FIGURE 2.44 Modifying the width of the tunnel in Badwater Basin
> allowed for better circulation of both the player and mine cart
> through the level and made gameplay less aggravating for the offensive
> team.
>
> mine tunnels a standard width that they had used for other basic maps.
> However, upon playtesting the level with the mine cart-pushing
> mechanic in place, they realized that tunnels had to be widened to
> accommodate both players and the cart. This seems like a small change,
> but it prevented a lot of aggravation from players that had been
> getting blocked out of tun- nels by the cart (Figure 2.44).
>
> This ties back to the idea of utilizing measurement systems for levels
> based on gameplay metrics. As level designers, it is our job to design
> to the realities of how player avatars and other gameplay elements
> move through levels. Traversing levels is comfortable when level
> spaces comfortably accommodate metrics. As we explore in later
> chapters, gameplay drama can be achieved when we create spaces that
> push metrics to the limit. Such spaces include gaps that require the
> farthest possible jump a char- acter can make, such as the one found
> in world 8-1 of *Super Mario Bros.* (Figure 2.45) or tight corridors
> that restrict movement in horror games, such as *Resident Evil*18
> (Figure 2.46).
>
> Designing to gameplay does not solely have to involve measurements
> either. It can also mean designing to specific character *abilities*
> such as special attacks or movement modes. Stealth games like *Metal
> Gear Solid*19 provide a great example of how to construct levels based
> on different types of character movement. In *Metal Gear Solid*, the
> player character, Solid Snake, has the ability to hide behind walls
> and look around corners.
>
> ![](./media/media/image145.jpeg){width="2.9111242344706914in"
> height="1.7285553368328959in"}
>
> FIGURE 2.45 This section of *Super Mario Bros.*'s level 8-1 pushes
> Mario's jump- ing metrics to their limit. The gap is 10 blocks wide, 1
> block longer than Mario's running jump distance of 9 blocks, so using
> the 1-block-wide middle island is necessary. Most strategies for
> crossing this gap call for a running jump to the middle island, and
> then another quick one off the 1-block-wide island so Mario's landing
> inertia doesn't launch the player into the pit.

![](./media/media/image146.jpeg){width="2.62615813648294in"
height="3.0533333333333332in"}

> FIGURE 2.46 Many hallways in *Resident Evil* are barely wide enough
> for two characters standing shoulder to shoulder. In this way, a
> single zombie in these hallways can become a significant threat for
> players trying to get past. This spatial condition also gives the game
> a claustrophobic atmosphere.
>
> This vastly changes the meaning of 90-degree corners when compared
> with other action games---they are strategic hiding places rather than
> just level geometry. As such, the nuclear weapons facility that makes
> up *Metal Gear Solid*'s environments has lots of these corners so
> players can sneak from place to place, looking around corners to find
> their next ref- uge. While not measurement or metric based, these
> kinds of layouts are based on the character's own *mechanics*, the
> gameplay actions that form the range of possibilities for how a
> character may act or interact with his or her environment.
>
> Level Design Parti
>
> Earlier we discussed the architect's parti, basic formal explorations
> that architects utilize to determine what shape or orientation they
> want their building to take. For level designers coming off of
> determining the core mechanics of their level, a parti is another
> valuable tool for developing the spatial layout of their level.
>
> Designing with parti is quite different than designing on graph paper
> or computer. Partis are meant to be sketches, and therefore will lack
> mea- surement. While this may seem contradictory to the rest of the
> advice in this chapter, sketching exercises allow designers to form
> ideas quickly before spending the time to plan measured versions of
> their designs. The key to a level designer's parti is to sketch
> *gameplay ideas as spatial dia- grams*. For example, a level design
> parti of the Badwater Basin level would be two large masses
> (representing the teams' base areas) with thinner zones of circulation
> in between the two to represent the mine cart track, and some smaller
> bases for BLU players to capture, similar to the diagram in Figure
> 2.43.
>
> In his discussions of level design from *Indie Game: The Movie*,
> Edmund McMillen argues that once a designer has created *environmental
> mechan- ics*, that is, interactive parts of a level that factor into
> gameplay, they should be usable in many different ways in order to be
> valuable. For e4 Software's mobile game *SWARM!*,20 a
> ball-roller/platformer game where players had to lure enemies into
> traps, programmer/designer Taro Omiya created many sketches of the
> electric fence traps to visualize the different uses they could have
> (Figure 2.47). Likewise, Omiya and others working on the game made
> formal partis on the computer and on paper to visualize spatial
> orientations of levels, such as downhill slides, floating islands, and
> platforming areas (Figure 2.48).
>
> ![](./media/media/image147.jpeg){width="3.8516765091863516in"
> height="1.9133333333333333in"}
>
> FIGURE 2.47 Once designers for *SWARM!* created the electric fence
> traps, they sketched many gameplay partis of them to visualize how
> they could be utilized through different levels.
>
> Pacing Your Levels with the *Nintendo Power* Method
>
> A downside to planning out individual bits of gameplay is not
> understand- ing how they relate to one another within a level. This is
> where drawing techniques for graph paper and other measurement-based
> tools come in. Arranging gameplay properly is known by level designers
> as *pacing*.
>
> Pacing is based on the concept that in order for gameplay action to
> seem exciting, it must be contrasted with moments of "quieter"
> gameplay, such as puzzle solving, exploring, or even playing with a
> character's movement possibilities. As we show in later chapters,
> spatial contrast is very impor- tant for building meaningful
> experiences in both games and architecture. As such, we must learn how
> to control how we pace our levels in games.
>
> In reality, the kind of top-down level design done on paper should
> occur from two different points of view: *macro-scale level design*
> and *micro-scale level design*. The parti for *TF2*'s Badwater Basin
> is a macro-scaled design, as it shows the entire level and diagrams
> how it creates the intended game- play. On the other hand, the partis
> of traps and level pieces from *SWARM!* are micro-scaled designs, as
> they show individual gameplay instances divorced from an entire level.
> Many new designers make the mistake of putting intense micro-scaled
> gameplay instances together in succession in their levels. Proper
> pacing would have gameplay points like this separated from one another
> by periods of quieter gameplay.
>
> To circumvent this, it is useful to use the *Nintendo Power* method of
> level design. *Nintendo Power* was a game strategy and news magazine
> published by Nintendo beginning in the late 1980s. For some time, it
> was
>
> ![](./media/media/image148.jpeg){width="2.7614807524059493in"
> height="1.5533333333333332in"}

![](./media/media/image149.jpeg){width="2.5955555555555554in"
height="3.6926520122484687in"}![](./media/media/image150.jpeg){width="2.303167104111986in"
height="1.3533333333333333in"}

> FIGURE 2.48 Formal partis for *SWARM!* show the visualization of
> different spatial orientations such as hills, tilted ledges, and
> others.
>
> ![](./media/media/image151.jpeg){width="3.152222222222222in"
> height="1.6116797900262467in"}
>
> FIGURE 2.49 Maps in *Nintendo Power* magazine show the entirety of a
> level and highlight important points of gameplay on each map.
>
> a valuable source of secret codes, hints, and tips on how to beat
> games on Nintendo consoles. For many games, *Nintendo Power* would
> publish detailed maps of levels with caption balloons that would
> highlight par- ticularly noteworthy or difficult points of gameplay
> (Figure 2.49). For level designers, these maps can be a valuable
> lesson on pacing.
>
> *Nintendo Power* maps show a level from a macro-scaled point of view,
> so a reader can see a game level in its entirety. At the same time, it
> high- lights important gameplay moments on the micro-scale so readers
> know what to look out for to reach secret rooms or beat difficult
> obstacles. It should also be noted that the highlight balloons on
> these maps were not butted against one another in quick succession,
> but rather spread evenly across a map. This is less a result of the
> magazine's publishing and more a result of proper pacing by the game
> designers. When designing levels, we can utilize the same mindset by
> treating our level drawings as ones from *Nintendo Power*, creating
> the overall scope of a level on a macro- scale and evenly spreading
> out micro-scaled areas of more intense game- play across the entire
> map. In between the "loud" gameplay moments should be circulation
> spaces⎯spaces for movement-based gameplay, movement-based obstacles,
> exploration, or even rest and recharging of the player character.
>
> Without quiet moments to contrast moments of high action in a level,
> the game can turn into a never-ending slog rather than an exciting
> experi- ence. Even with the most careful planning, however, a designer
> is bound to miss something. That is why it is important to play a game
> as much as possible and have others play it, which will take us to our
> next level design workflow.
>
> Iterative Design with Playtesting
>
> Iterative design is a term borrowed from human-computer interface
> design. It describes a cyclical design process where the designer
> produces a prototype of his or her work, tests whether a user can
> properly interact with it, evaluates the results, makes changes to the
> design, and tests it with a user again. It is not unlike the
> scientific method, where a scientist tests a hypothesis with repeated
> experimentation.
>
> Game designers test their ideas by holding playtests of their games.
> Salen and Zimmerman call game design a *second-order design* problem.
> They say in *Rules of Play*, "You are never directly designing the
> behav- ior of your players. Instead you are only designing the rules
> of the sys- tem."21 Salen and Zimmerman are pointing out that
> designing a game is very different than designing a directly relatable
> object such as a cup or a chair⎯you are creating a context for players
> to inhabit. This directly ties to the idea that a game level is a
> medium of communication between play- ers and designers.
>
> Much like how an architect will bring clients in to see and evaluate
> work, game designers bring their eventual clients⎯their players⎯in to
> playtest their game. To understand whether the experience you intend
> happens in your game levels, it is important to watch others play your
> game in both non-digital and digital forms, depending on your stage of
> development. As you watch people play your levels, keep these things
> in mind:
>
> *Do they understand how to play the level?* When discussing adjustment
> of behavior, we saw that teaching is an important mission of level
> design. If a player does not understand a puzzle that you intend to
> repeat, he or she may need a better or more transparent introduction
> to the mechanic before reaching the iteration of it that he or she is
> stuck on.
>
> *Is the level too hard for the player?* This mainly applies to early
> levels of a game, though you should always avoid sudden increases in
> difficulty without proper balancing or player preparation. If a player
> is getting stuck on a challenge or puzzle ten minutes into your game,
> you should perhaps place that challenge later in the game or build
> easier levels and put them before the challenge the player is stuck
> on. Playtesting is important because as you play your own game, you
> become very good at it and can no longer see when things are too hard.
>
> *Do not interfere with their play.* When people buy your game, they
> will not have you there to explain how it is supposed to be played.
> Thus you should not stop a playtester to explain what he or she is
> supposed to do. If he or she cannot figure it out, you should add more
> teaching moments to your levels.
>
> *Embrace happy accidents.* Sometimes playtesters reveal a strategy,
> solve a puzzle in a unique way, or "game" the system to create new
> abili- ties. For example, entire areas of *SWARM!* levels are
> skippable if you know where to jump from. When you see players
> performing an action or using a level in a way you did not intend,
> evaluate whether it is game breaking. If it is not, but could instead
> be an interesting secret to find, leave it in.
>
> *Playtest for the current stage of development.* Lead playtesters to
> give you feedback on issues that match your stage in development.
> Major gameplay feedback should occur early before assets are cre-
> ated, while late feedback should focus on finding *bugs*, errors that
> can inhibit the experience of, halt any progress in, or even crash the
> game. Feedback on gameplay mechanics or art, for example, has no place
> a month before launch when testing should focus on finding bugs. Ask
> playtesters prepared questions relating to the information you want
> from them or create a paper survey for them to fill out.
>
> *Ask for additional comments, but stick to your guns.* While you want
> focused feedback, it is good to get additional comments in case play-
> testers have any happy accident statements that could help you out. Be
> prepared, though, for a slew of ridiculous suggestions. Playtesters
> are often very enthusiastic to help with the development of a game and
> will give design input of "things you should totally put in the game."
> Learn to properly vet these statements for things that can help in
> that stage of development versus the ones that will break your game's
> core vision. Also learn to dismiss bad ideas in a friendly and
> non-condescending way.
>
> As playtesters try your levels throughout your process, document what
> went well with each prototype and what could be changed or improved.
> Change your design and have someone playtest your next prototype. The
> next two sections will discuss prototypes of two kinds: non-digital
> and digital.
>
> Non-Digital Prototypes
>
> For years, game developers did not playtest a game until it was in
> *beta* stage, that is, the stage prior to release where asset
> production is already complete. This can be a dangerous way to
> playtest a game, as it is too late to fix fundamental design issues.
> In the last few years, a great deal has been written on testing
> throughout the design process, starting with non- digital prototypes
> of games. Even before game ideas are put into a com- puter, designers
> can use non-digital prototypes to explore the playability of their
> games.
>
> Most publications detail non-digital prototypes for game mechan- ics.
> However, level designers can utilize non-digital prototypes as well in
> certain types of games. In her book *Game Design Workshop*,22 Tracy
> Fullerton describes how EA utilizes a real-life sandbox to test levels
> for the *Medal of Honor* series. Designers utilize plastic trees, toy
> army men, and battlefield models to draft exterior levels. The authors
> also describe a board game prototype of a first-person shooter game,
> where the design- ers have defined movement rules for players moving
> army men around a hexagonal grid (Figure 2.50).
>
> Like the *Nintendo Power* method, non-digital prototypes can define
> gamespaces on both the macro and the micro scale. Student projects
> from the Introduction to Game Design course at George Mason
> University,23 for example, show that non-digital prototypes can reveal
> spatial realities of different parts of games. One prototype required
> players to progress their knight character through different stages of
> a Candy Land-like board until they reached the princess at the end.
> The designers, seeking a story- heavy role-playing adventure game,
> opted for a board with a linear path with minimal forks. In many ways,
> this board is an interactive parti for the

![](./media/media/image152.jpeg){width="2.993674540682415in"
height="1.08in"}

> FIGURE 2.50 A non-digital prototype of a first-person shooter
> utilizing a hex- agonal grid and army men. Designers place matchsticks
> on the board to define walls. The matchsticks are ideal for a simple
> prototype, as they can be easily picked up and moved to try different
> spatial articulations.
>
> entire game, showing the designer's intent of creating a linear
> experience based on specific story beats rather than player choice. As
> a demonstration of the game environment on a macro level, it allows
> players to play with the linear progression of general gameplay
> situations but not dig deeply into each one.
>
> A different student project prototyped a stealth game where players
> must elude guards, rescue their fellow prisoners, and escape a prison
> yard. This game focuses on micro-level gameplay prototyping by allow-
> ing designers to explore issues such as enemy movement and charac- ter
> interaction in a single room of the prison. The version demonstrated
> in the class utilized a completely open room devoid of any walls, as
> the designers were focused on defining how characters would move.
> However, further iterations of the board could potentially explore how
> the movement rules could work in more complex hallway and cell block-
> like environments.
>
> While non-digital prototypes can offer an abstracted trial of macro
> and micro spatial gameplay, digital prototypes allow designers to test
> the gameplay of specific environments through a process called
> *whiteblocking*.
>
> Digital Prototypes with Whiteblocking
>
> When developers have moved from prototyping off the computer to pro-
> totyping in digital form, they create test levels through a process
> known as whiteblocking. Whiteblocking is when a level designer creates
> a level out of simple geometry, most often white or textured blocks
> (thus the name), to test whether levels accomplish the gameplay goals
> he or she wants. Early on in the design process, when designers are
> trying to define gameplay metrics of player characters and other
> things, whiteblocking can help determine what gameplay measurements
> should be. Designers can draft the spatial characteristics of their
> levels in a parti-like way, testing the sizes and shapes of certain
> environments for different gameplay experi- ences, before specific
> environmental art is added to a level (Figure 2.51).
>
> The geometry used to whiteblock level spaces is usually the simplest
> needed to simulate the *colliders* that will be used in the eventual
> final level design. Colliders are a component of objects in game
> engines that simulate the interaction between physical objects. A box
> collider attached to a piece of level geometry, for example, will
> cause that object to interact with other objects as though it is the
> shape of a six-sided box, regardless of the shape of the actual
> environmental art (Figure 2.52). Colliders can be simple geo- metric
> shapes or can be made to tightly fit organic shapes.
>
> ![](./media/media/image153.jpeg){width="2.8579943132108485in"
> height="2.14in"}

![](./media/media/image154.jpeg){width="2.8533333333333335in"
height="2.14in"}

> FIGURE 2.51 Whiteblocking done for *SWARM!* shows how an important
> sec- tion of a level meant to teach players how to kill enemies was
> thoroughly tested in simple geometry before environment art was added.
>
> Valve uses whiteblocking extensively in its level design process. The
> construction rules for engine primitives in their level editor,
> Hammer, allow rapid 3D level prototyping through simple and precise
> building. Hammer's primitives, called brushes, are used to roughly
> define level spaces, which are then playtested to see if the intended
> experience is cre- ated. Level designers see what worked properly and
> what did not, and then change the spaces by editing the brushes. When
> the designers find themselves editing little of major spaces and
> instead focusing on smaller details, the level is ready for
> environment art.
>
> As an iterative process, whiteblocking begins with almost parti- like
> interactive forms of levels and moves designers toward more art
>
> ![](./media/media/image155.jpeg){width="2.5003991688538934in"
> height="2.6066666666666665in"}
>
> FIGURE 2.52 This plant has a box collider attached to it. Though its
> 3D model has an organic shape, player objects in a game will interact
> with it as though it were a rectangular solid.
>
> and ornament-centric design decisions that are not unlike interior
> design. As level geometries become better defined, standard pieces of
> environ- ment art can be defined as well, eventually becoming the
> building blocks of levels. Metric-centric environment art is an
> important part of the design process that is discussed in the next
> section.
>
> Modular Level Design
>
> An advantageous aspect of building levels with engine primitives is
> that these primitives are standardized within the engine and easily
> repeatable. They are *modular*, that is, premade parts that can be
> copied, assembled, disassembled, and moved easily. Since the
> Industrial Revolution, buildings have been made of modular elements.
> Many of these are *prefabricated*, cre- ated at a factory and
> assembled on the building site. Modernist architects were great
> proponents of modularity in their buildings. Phillip Johnson and
> Ludwig Mies Van Der Rohe, for example, are famous for designing
> buildings with prefabricated steel and glass components. Le Corbusier
> designed Unite D'Habitacion, an apartment building where the apart-
> ments were created as modular units and stacked together (Figure
> 2.53).
>
> We have used LEGO building blocks as a metaphor for level design;
> modularity is the reason for this. Game development is a
> work-intensive process, and an intelligent designer will utilize
> easily repeatable game
>
> ![](./media/media/image156.jpeg){width="2.2636800087489064in"
> height="2.4031069553805775in"}
>
> FIGURE 2.53 An apartment cross-section and model sketch of Unite
> D'Habitacion by Le Corbusier.
>
> objects and textures to lessen the need for constant recreation of art
> assets. If designers create a set of modular pieces like those shown
> in Figure 2.41, levels can be assembled like sets of LEGOs rather than
> difficult-to-change custom artworks.
>
> Creating modular assets can also aid the metric-based measurement
> methods outlined earlier in the chapter. The designers of *SWARM!*
> uti- lized modular tiles for some of their non-organic level designs.
> Building in predefined tiles allowed for the easy measurement of game
> environments such as skate parks and mazes. For example, the designers
> realized that two-unit-wide tiles was the smallest unit that could be
> balanced on by players using the game's tilt controls without the game
> feeling unfairly dif- ficult. For labyrinth-like puzzles where the
> player had to navigate a narrow maze without falling into electrified
> floors or pools of acid, the two-unit tiles were used to build the
> ledges.
>
> Even for less measurement-based pieces, such as organic landmasses and
> plants, having modular pieces made construction of *SWARM!* levels
> simple. Less measurement-based objects like landmasses and trees could
> be scaled to any size without the art looking awkward compared to
> other objects. They could also be rotated in any way the designers
> wished, should up- or downhill areas be required for a level.
>
> Architects track modular elements of their buildings through documents
> called *building schedules*. A schedule is a chart that specifies
> prefabricated
>
> products, such as doors, windows, or plumbing fixtures, the sizes of
> such products, and where they should go in the building (Table 2.1).
> The modu- lar pieces used by level designers can be documented very
> similarly, espe- cially if the pieces follow measurement-based
> construction systems.
>
> In game art direction, it is common to utilize *style
> guides*---documents that establish color, graphics, measurement, and
> other artistic standards--- for maintaining graphic consistency with a
> team. Level design schedules can offer similar utility for level
> construction. A schedule for the half-pipe shown in Figure 2.54 might
> look like that found in Table 2.2.
>
> Even for scale-less pieces such as trees and plants, schedules can
> help establish the style guide for a level by listing the pieces that
> will make it up.
>
> TABLE 2.1 Door Schedule

+-----+---------+------------+-------+---------+-------------+------+
| **D |         | > **Door   | > **  | >       | > **Door    | >    |
| oor |         | >          | Frame | **Frame | > Opening   |  **H |
| Qu  |         | Material** | > T   | > Mat   | > Size**    | DW** |
| ant |         |            | ype** | erial** |             | >    |
| ity |         |            |       |         |             | >    |
| Typ |         |            |       |         |             |  **S |
| e** |         |            |       |         |             | et** |
+=====+=========+============+=======+=========+=============+======+
| 1   | 1       | > Wood     | A     | > HM    | > 3′0″ ×    | 05   |
|     |         |            |       |         | > 7′0″      |      |
+-----+---------+------------+-------+---------+-------------+------+
| 2   | 10      | > WD and   | A     | > HM    | > 3′0″ ×    | 14   |
|     |         | > TG       |       |         | > 7′0″      |      |
+-----+---------+------------+-------+---------+-------------+------+
| 3   | 1       | > Wood     | A     | > HM    | > 3′6″ ×    | 03   |
|     |         |            |       |         | > 7′0″      |      |
+-----+---------+------------+-------+---------+-------------+------+

![](./media/media/image157.png){width="3.0113921697287838in"
height="2.2466666666666666in"}

> FIGURE 2.54 A half-pipe level from a 3D game.
>
> TABLE 2.2 Level Tile Schedule, *SWARM!* Level 1−3
>
> **Quantity Model Type Model Name Location**
>
> 15 Half-pipe side Skatepark01_2x2.blend Skate park 2
>
> 8 Half-pipe ground CityFloor_Concrete_2x2.blend Skate park 2
>
> 4 Electric fences CityTrap_ElectricFence02_2tile.blend Skate park 2
>
> In this way, schedules are useful for both listing the pieces that
> will make up certain environments and assisting with art direction.
>
> Now that we have explored several workflows for level design, we will
> demonstrate the tools in several popular game engines that more
> specifi- cally detail how levels are constructed.

## ENGINE-SPECIFIC METHODOLOGIES

> Just as there are a great number of level design methodologies, there
> are also many game engines that game designers can choose from. While
> it is outside the scope of this book to give specific tutorials on any
> one engine (there are many other excellent books that do that at great
> length), we will learn how an architectural design method can apply to
> engines actually used for game development. For maximum benefit, we
> explore four popu- lar engines, Game Maker, the Unreal Development Kit
> (UDK), Source's Hammer Editor, and Unity, to discover engine-specific
> factors that will influence how you design your own game levels. It
> should be noted that this section will address engine-specific methods
> and concerns, so the use of importing modular objects from 3D art
> programs---which each engine is capable of---will be explored only for
> engines where it is an absolutely necessary part of the level
> construction process. If you are using engines other than the ones
> listed here, there should still be information that you can migrate to
> your own software of choice.
>
> Game Maker
>
> Game Maker is a 2D-focused game engine created by YoYo Games. For many
> new designers, it is a great piece of software to learn with. Two-
> dimensional games are often much simpler to create than full 3D games
> due to both programming complexity and the amount of art required for
> a 3D game to look visually complete (minimalist art styles notwith-
> standing). Game Maker earns its reputation as a great learning engine
> by allowing users to create games with drag-and-drop logic elements
> rather than requiring the use of a scripting language. As designers
> gain skill with Game Maker, they can utilize Game Maker Language
> (GML), the engine's internal scripting language, and also create
> simple three-dimensional games with its limited 3D capabilities
> (Figure 2.55).
>
> For designers utilizing the architectural methods discussed earlier in
> this chapter, especially those centered on grid-based measurement,
> Game Maker is an excellent tool for practicing level design. Levels in
> Game Maker are constructed as rooms, which are analogous to the scenes
> used in other
>
> ![](./media/media/image158.png){width="4.51988188976378in"
> height="2.2733333333333334in"}
>
> FIGURE 2.55 The Game Maker interface with a 2D game level being built
> according to power of 2 measurements.
>
> game engines. When creating a new room, the window for that room
> displays a grid spaced according to power of 2 pixel measurements,
> such as 16 × 16 (the default), 32 × 32, 64 × 64, and so on. Snap
> settings can be set to non-power of 2 measurements, though such
> measurements require more memory for a computer to process than power
> of 2.
>
> Assuming the use of these units, 2D level objects can easily be drawn
> to conform to grid square size and placed on the room grid itself.
> Also, following the Game Maker grid system helps plan out game charac-
> ter movements in the same way that graph paper can---according to
> measurement-based movement metrics. By understanding how your
> character moves in relation to the grid squares, level objects can be
> sized and spaced accordingly.
>
> Unreal Development Kit (UDK)
>
> The first of several 3D engines this section will examine, the UDK is
> a free-for-non-commercial-use version of Epic Games's Unreal Engine 3,
> the engine originally used to create *Unreal Tournament 3*. The UDK is
> a popular engine thanks to its powerful level editor and advanced
> lighting capabilities. The level editor allows for the quick creation
> of levels within the engine itself with UDK's *binary space
> partitioning (BSP) brushes*. The default texture settings for the BSP
> brushes result in nicely textured sur- faces, lessening the need for
> applying textures to simple objects via the *UV unwrapping* functions
> of 3D art programs (Figure 2.56).
>
> ![](./media/media/image159.jpeg){width="4.049678477690288in"
> height="2.453333333333333in"}
>
> FIGURE 2.56 A screenshot of the UDK interface while editing a hollow
> room. The checkers on surfaces demonstrate how textures automatically
> tile across in-engine objects, greatly lessening the need for UV
> mapping of environmental geometry.
>
> When editing in UDK, as with the other engines we will discuss,
> understanding the unit system is vital for sizing objects. In UDK, a
> char- acter is typically 96 UDK units tall. While this measurement
> does not have the simplicity of power of 2 settings employed by
> engines like Game Maker, designers can still use it as a base for
> their work. When using mod- els imported from 3D art programs, which
> UDK refers to as *static meshes*, to build levels, it is recommended
> that you use a scaling model to generate metric-appropriate static
> meshes.
>
> Source's Hammer Level Editor
>
> Source debuted in 2004 with the games *Counter Strike: Source* and
> *Half- Life 2*. Like Unreal Engine 3, which debuted the same year, it
> remains a popular choice for designers thanks to consistent updates.
> Source is usable by anyone with a copy of a Source-built game and is
> downloadable on Valve Corporation's Steam distribution platform.
>
> Source's internal level editing program, Hammer, combines much of what
> makes engines like Game Maker and UDK appealing. Like UDK, Hammer is a
> 3D-focused engine and allows users to edit geometry with geometric
> primitives called *brushes*. Like Game Maker, it features a power of
> 2-based grid system for editing levels with controllable snaps (Figure
> 2.57).
>
> ![](./media/media/image160.jpeg){width="4.506352799650044in"
> height="2.66in"}
>
> FIGURE 2.57 A screenshot of Hammer, showing a simple level built out
> of brush primitives. Hammer's brushes are editable, so objects such as
> arches and domes can be built in-engine.
>
> Hammer's snap settings are vital for creating levels in the engine, as
> environments must be fully closed in order to be *compiled*, or
> processed into levels that can be run in Source games. The snap
> settings help users build levels that work around this limitation, but
> that also help create metric-appropriate geometry.
>
> Hammer's texture system also conforms to its power of 2 focus. By
> default, textures imported into Hammer appear at a size dependent on
> their actual file size. For example, a 128 × 128 pixel texture will
> always import at the same size. While these sizes are editable on
> individual brush *faces*, or sides, the default sizes are consistent
> such that the editor even includes test textures that feature notes on
> texture size (Figure 2.58). This level of consistency allows for
> powerful metric and measurement-based editing.
>
> Unity
>
> The final engine we will discuss is Unity, a 3D-focused engine that
> has become popular among both large and small studios. Unlike the
> other 3D engines discussed here, Unity was not developed as a tool for
> any one spe- cific game, but is rather a tool for creating an array of
> different game types. This lack of specialization is a double-edged
> sword: the engine allows for the flexible creation of many styles of
> games but lacks the level editors
>
> ![](./media/media/image161.jpeg){width="4.052459536307961in"
> height="2.446665573053368in"}
>
> FIGURE 2.58 Textures imported into Hammer at sizes consistent with
> their file sizes. For texture and unit planning, the engine includes
> annotated textures that show how big each object is.

![](./media/media/image162.jpeg){width="2.432415791776028in"
height="1.909291338582677in"}![](./media/media/image163.jpeg){width="1.622415791776028in"
height="2.2853608923884514in"}![](./media/media/image164.jpeg){width="2.432415791776028in"
height="0.38090223097112863in"}

> FIGURE 2.59 A screenshot of Unity. The level prototype shown is
> constructed out of modular objects prefabricated in 3D art programs
> and then arranged in the engine.
>
> that the other two 3D engines---both originally created for
> first-person shooters---have internally (Figure 2.59).
>
> As such, level editing in Unity requires an extra bit of planning on
> the part of the designer. Unity uses its own system of units that are
> equal to 1 meter each, so building a measurement-based planning system
> is simple.
>
> Unlike UDK or Source, however, Unity's 3D primitives lack the UV
> mapping to be effective brush geometry. Unity primitives are *planar
> mapped*, which means that textures are projected onto them from one
> angle. If, for example, a cube primitive is scaled so it becomes a
> rectangu- lar solid, the textures on the short sides will appear
> squeezed.
>
> Unity is an engine where modular prefabricated objects are vital. This
> requires a bit of extra time spent in 3D art programs and with UV
> unwrap- ping, but the result will pay off for creating
> metric-appropriate levels that can be rapidly prototyped from graph
> paper maps. Examples shown ear- lier in this chapter reflect this type
> of prefabrication: creating orthogonal tile objects for man-made
> environments and arrangeable plants, trees, and islands for organic
> environments. Unity even aids this kind of level construction with
> *vertex snaps*, a system that allows users to snap objects precisely
> to the sides and corners of other objects.

## SUMMARY

> There is a wide variety of tools for the study, planning, and
> execution of game levels that can work together to create better game
> experiences. By understanding the different methods for drawing and
> diagramming space, we can become better observers of gamespace. By
> planning levels in such a way that we focus on measurements, we can
> prepare for the realities of gameplay. Implementing these findings in
> game engines and prototyping them in an iterative process can ensure
> that our game levels meet our original experiential goals. Finally,
> exploring different engines not only will allow us to find the best
> tool to implement our ideas, but also can help us modify our design
> method to fit within the constraints of each software.
>
> In the next chapter, we take these lessons and explore the differ- ent
> types of spaces found in both real and game worlds. Through this
> exploration we will discover how to utilize these spatial types, and
> the points of view from which we see them, to create meaningful
> gameplay experiences.

## ENDNOTES

1.  *Indie Game: The Movie*. Directed by Lisanne Pajot, performed by
    Jonathan Blow, Phil Fish, Edmund McMillen, and Tommy Refenes.
    Flutter Media, 2012. Film.

2.  Kremers, Rudolf. *Level Design: Concept, Theory, and Practice*.
    Wellesley, MA: A.K. Peters, 2009, p. 33.

3.  Bogost, Ian. *Persuasive Games: The Expressive Power of Videogames*.
    Cambridge, MA: MIT Press, 2007.

4.  Ching, Francis D.K., and Steven P. Juroszek. *Design Drawing*. New
    York: John Wiley & Sons, 1998, p. 6.

5.  Ching, Francis D.K., and Steven P. Juroszek. *Design Drawing*. New
    York: John Wiley & Sons, 1998, p. 8.

6.  Ching, Francis D.K., and Steven P. Juroszek. *Design Drawing*. New
    York: John Wiley & Sons, 1998, pp. 29--31.

7.  Ching, Francis D.K., and Steven P. Juroszek. *Design Drawing*. New
    York: John Wiley & Sons, 1998, pp. 43--45.

8.  Le Corbusier. *Towards a New Architecture*. New York: Dover
    Publications, 1986, p. 47.

9.  Frederick, Matthew. *101 Things I Learned in Architecture School*.
    Cambridge, MA: MIT Press, 2007, p. 68.

10. *Half-Life 2: Raising the Bar*. Roseville, CA: Prima Games, 2004.

11. Casali, Dario. Interview by author, personal. Valve Corporation,
    Bellevue, WA, October 27, 2008.

12. Jarvinen, Aki. GameGame. *GameGame*. <http://gamegame.blogs.com/>
    (accessed January 3, 2013).

13. *Super Mario Bros.* Nintendo (developer and publisher), September
    13, 1985. Nintendo Entertainment System game.

14. *The Legend of Zelda*. Nintendo (developer and publisher), February
    21, 1986. Nintendo Entertainment System game.

15. *Katamari Damacy*. Namco, Now Productions (developer), Namco
    (publisher), September 22, 2004. Sony Playstation 2 game.

16. *Angry Birds*. Rovio Entertainment (developer), Chillingo
    (publisher), December 11, 2009. Mobile device game.

17. *Team Fortress 2*. Valve Corporation (developer and publisher),
    October 9, 2007. PC game.

18. *Resident Evil*. Capcom (developer and publisher), March 22, 1996.
    Sony Playstation game.

19. *Metal Gear Solid*. Konami Computer Entertainment Japan (developer),
    Konami (publisher), September 3, 1998. Sony Playstation game.

20. *SWARM!*. e4 Software (developer and publisher), January 2, 2013.
    Mobile device game.

21. Salen, Katie, and Eric Zimmerman. *Rules of Play: Game Design
    Fundamentals*. Cambridge, MA: MIT Press, 2003, p. 168.

22. Fullerton, Tracy, Christopher Swain, and Steven Hoffman. *Game
    Design Workshop: A Playcentric Approach to Creating Innovative
    Games*. 2nd ed. Amsterdam: Elsevier Morgan Kaufmann, 2008.

23. From the Introduction to Game Design course at George Mason
    University's Computer Game Design Program. Taught by Prof.
    Christopher Totten.

> INTERVIEW WITH ROBIN RATH
>
> *CEO, Pixel Press*
>
> Robin Rath is a web developer, product strategist, and game developer.
> In 2013, he successfully raised crowdfunding money on Kickstarter to
> create Pixel Press, a game development platform for mobile devices
> that allows users to design lev- els by drawing them on graph paper
> and photographing them. The first toolset, Pixel Press Floors, an
> application for creating platformer games, will be released for iOS in
> early 2014 and followed shortly by an adventure game tool.
>
> *Can you name a game, level, or level designer (or multiples of each)
> whose work has left an impression on you? Why?*
>
> I use this one a lot---*Metroid*---not only because it had such a big
> impact on my childhood, but because I have gone back and played it as
> an adult, and explored it in more detail since working on my latest
> project. I am infinitely impressed by how simple, but still
> challenging, it is. In reality, there is not much different going on
> from area to area with the exception of visuals and enemy
> physics---the main difference being level design. It's amazing how
> much the level design itself impacts the experience in a game like
> *Metroid*.
>
> *Are there any media outside of gaming that you find inspire your
> work?*
>
> I'm always inspired by the simplicity that web applications can
> embrace and achieve, and how that can be applied to games.
>
> *Describe your level design process---how do you begin? What tools do
> you use (on or off the computer)?*
>
> My video game background is likely not as extensive as most others in
> your book, but even as a kid the video game design I did was always on
> pencil and paper. I've since been heavily involved in building many
> web applications, and that experience has very much carried over into
> creating the first drafts of an application. I feel strongly that the
> mindset achieved during the true sketching process of a project is
> critical because it starts the project off in the most fundamental way
> possible.
>
> *What is your process for playtesting your levels?*
>
> From my experience with web application development, it's about
> starting early and often. With *Pixel Press*, we are providing testing
> tools very early on in the process, before the user gets to the design
> stage. Playtesting occurs in your head during the sketch process, and
> should continue throughout the project.
>
> *Do you find art and atmospheric effects an important tool for
> communicating with players? Any specific examples?*
>
> Absolutely, the idea of jump and running around in these foreign
> worlds is familiar in concept, but doesn't necessarily create a
> mood---atmosphere
>
> creates the mood that makes the whole thing more believable, or if not
> believable, then purely fascinating and interesting.
>
> *How do you teach players to utilize your levels (without use of the
> GUI)?* The mechanic you now find so often in video games, where the
> first few levels teach you how the game works, has been perfected in
> some instances---it works the best with simple platformers, as seen
> with games like *League of Evil 3* on the iPhone. I think following
> this model for other genres is the way to go.
>
> *How do you entice players to explore game levels (without use of the
> GUI)?* This is just about smartly stringing together objectives and
> enticing explora- tion by providing tools or objectives that build on
> each other. Lots of games do this well, when combined with a
> compelling storyline as well.
>
> *If a player is lost in one of your levels, how can he find his way
> back to where he is supposed to be (without using the GUI)?*
>
> If you've done it right, there were memorable visual clues that will
> help them get back without much trouble. This, of course, is easier
> with some games than others, but I think is an art in and of itself
> that games like the *Halo* series sometimes do really well, and
> sometimes don't.
>
> *What "laws of level design" have you developed in your own work that
> any designer should know? What should they avoid?*
>
> Understand the tools that you have at your disposal, and find
> interesting ways to use them and test your hypothesis to see if it's
> fun. Not sure other than pure experience that there is any other way
> to do it.
>
> *Your design app, Pixel Press, utilizes graph paper as a tool for
> level design.*
>
> *Describe how you came to the decision to utilize this format.*
>
> I've always felt that putting your head in a very fundamental place at
> the beginning of the project is the best place to start. For level
> design, you want to be very deliberate with what you are doing to
> create the most interest- ing challenge that rewards the user for
> succeeding. Working in a drag-and- drop environment gives the user too
> much power and they don't spend the time thinking about what they are
> doing, they are already in design mode. However, the
> alternative---creating a game from scratch using code
> (programming)---is beyond the mental capacity (or at the least,
> patience) for most people; drawing is a good middle ground. The graph
> paper also gives the whole process structure, which is a welcome
> experience for most people.
>
> *How important is it that users pay attention to the movement
> capabilities of their game characters? What can be accomplished
> through designing for these capabilities?*
>
> Understanding how the character can work within the environment is
> critical. If the character can only run and jump, and jump so high,
> you really need to know that, not just to avoid creating
> impossible-to-pass circumstances, but also to make circumstances fun.
> Beyond that, if the character has additional
>
> capabilities that can be combined with run and jump, the possibilities
> to create even more complex challenges really opens up.
>
> *Pixel Press allows users to create different gameplay elements by
> drawing their levels with specific signs or visual elements. How is
> that use- ful to designers?*
>
> If we are talking about designers in the sense of the visual design of
> the game, then giving them tools to create games themselves is very
> powerful. Since most designers don't code (program), giving them this
> control is appealing.
>
> *Beyond Pixel Press, do you believe the methodology you've developed
> will be useful in other products?*
>
> We're focused on the platformer (run and jump) genre to start, but of
> course there are many other genres we can work around---adventure,
> role-playing game (RPG), racing, tower defense---just to name a few.
> We can even offer experiences that offer simple enhancements, such as
> drawing your own *Madden Football* play. Beyond that, we've talked
> about other industries, such as architecture, interior design, and
> manufacturing, but we've decided to start with the fun part first.

