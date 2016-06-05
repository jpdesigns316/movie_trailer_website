import movie
import fresh_tomatoes


gods_not_dead = movie.Movie(
    "God's Not Dead",
    "PG",
    113,
    "Shane Harper, Kevin Sorbo, David A.R. White",
    '''College philosophy professor Mr. Radisson's curriculum is challenged
    by his new student, Josh, who believes God exists.''',
    "http://www.impawards.com/2014/posters/gods_not_dead.jpg",
    "https://www.youtube.com/watch?v=bMjo5f9eiX8")

existinz = movie.Movie(
    "eXistinZ",
    "R",
    97,
    "Jude Law, Jennifer Jason Leigh, Ian Holm ",
    '''Video game designer Allegra Geller (Jennifer Jason Leigh) has
    created a virtual reality game called eXistenZ. After a crazed fan
    attempts to kill her, Allegra goes on the run with Ted (Jude Law),
    a young businessman who falls into the role of bodyguard. In an
    attempt to save her game, Allegra implants into Ted's body the
    video game pod that carries a damaged copy of eXistenZ. Allegra
    and Ted engage in a series of experiences that blur the lines
    between fantasy and reality.''',
    "http://www.impawards.com/1999/posters/existenz_ver1.jpg",
    "https://www.youtube.com/watch?v=HAdbdUt_h9M")


aristocats = movie.Movie(
    "Aristocats",
    "G",
    78,
    "Phil Harris, Eva Gabor, Sterling Holloway",
    '''When a retired opera singer leaves her inheritance to her cat,
    Duchess (Eva Gabor), and three kittens, the woman's butler drugs
    the cats and abandons them in the countryside in order to inherit
    the fortune himself. Lost in unfamiliar territory, Duchess and the
    kittens meet Thomas O'Malley (Phil Harris), an alley cat willing to
    help them return to their home in Paris. They meet several kooky
    characters along the way, including two English geese and an alley
    cat jazz band.''',
    "http://www.impawards.com/1970/posters/aristocats.jpg",
    "https://www.youtube.com/watch?v=U5cJlj7YGt8")

jurrassic = movie.Movie(
   "Jurassic Park",
   "PG-13",
   127,
   "Sam Neill, Laura Dern, Jeff Goldblum",
   '''In Steven Spielberg's massive blockbuster, paleontologists Alan
   Grant (Sam Neill) and Ellie Sattler (Laura Dern) and mathematician
   Ian Malcolm (Jeff Goldblum) are among a select group chosen to tour
   an island theme park populated by dinosaurs created from prehistoric
   DNA. While the park's mastermind, billionaire John Hammond (Richard
   Attenborough), assures everyone that the facility is safe, they find
   out otherwise when various ferocious predators break free and go on
   the hunt.''',
   "http://goo.gl/BEHv3s",
   "https://www.youtube.com/watch?v=QWBKEmWWL38")

ghostbusters = movie.Movie(
   "Ghostbusters",
   "PG",
   105,
   "Bill Murray, Dan Aykroyd, Sigourney Weaver",
   '''After the members of a team of scientists  (Harold Ramis, Dan
   Aykroyd, Bill Murray) llose their cushy positions at a university in New
   York City, they decide to become "ghostbusters" to wage a high-tech battle
   with the supernatural for money. They stumble upon a gateway to another
   dimension, a doorway that will release evil upon the city. The Ghostbusters
   must now save New York from complete destruction.''',
   "http://media.theiapolis.com/d4/h1AW/i2CQE/k4/l2DPX/wXA/ghostbusters.jpg",
   "https://www.youtube.com/watch?v=vntAEVjPBzQ")

lion_king = movie.Movie(
    "Lion King (1994)",
    "G",
    89,
    "Matthew Broderick, Jeremy Irons, James Earl Jones",
    '''This Disney animated feature follows the adventures of the young lion
    Simba (Jonathan Taylor Thomas), the heir of his father, Mufasa (James Earl
    Jones). Simba's wicked uncle, Scar (Jeremy Irons), plots to usurp Mufasa's
    throne by luring father and son into a stampede of wildebeests. But Simba
    escapes, and only Mufasa is killed. Simba returns as an adult (Matthew
    Broderick) to take back his homeland from Scar with the help of his friends
    Timon (Nathan Lane) and Pumbaa (Ernie Sabella).''',
    "https://www.movieposter.com/posters/archive/main/108/MPW-54063",
    "https://www.youtube.com/watch?v=f0fReuRs890")

tron = movie.Movie(
    "Tron",
    "PG",
    96,
    " Jeff Bridges, Bruce Boxleitner, David Warner",
    '''When talented computer engineer Kevin Flynn (Jeff Bridges) finds out
    that Ed Dillinger (David Warner), an executive at his company, has been
    stealing his work, he tries to hack into the system. However, Flynn is
    transported into the digital world, where he has to face off against
    Dillinger's computerized likeness, Sark, and the imposing Master Control
    Program. Aided by Tron (Bruce Boxleitner) and Yori (Cindy Morgan), Flynn
    becomes a freedom fighter for the oppressed programs of the grid.''',
    "http://www.impawards.com/1982/posters/tron.jpg",
    "https://www.youtube.com/watch?v=1fSUos8x73I")

hook = movie.Movie(
    "Hook",
    "PG",
    142,
    "Dustin Hoffman, Robin Williams, Julia Roberts",
    '''When his young children are abducted by his old nemesis, Capt.
    Hook (Dustin Hoffman), middle-aged lawyer Peter Banning (Robin Williams)
    returns to his magical origins as Peter Pan. Peter must revisit a foggy
    past in which he abandoned Neverland for family life, leaving Tinkerbell
    (Julia Roberts) and the Lost Boys to fend for themselves. Given their
    bitterness toward Peter for growing up -- and their allegiance to their
    new leader, Rufio -- the old gang may not be happy to see him.''',
    "http://ashvegas.com/wp-content/uploads/2014/05/936full-hook-poster.jpg",
    "https://www.youtube.com/watch?v=LxnR9e7M8Vw")

#  A list of the movie objects
movie = [aristocats, existinz, ghostbusters, gods_not_dead, hook, jurrassic,
         lion_king, tron]
fresh_tomatoes.open_movies_page(movie)
