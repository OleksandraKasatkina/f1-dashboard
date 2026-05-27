CURRENT_YEAR = 2026
AVAILABLE_YEARS = list(range(2018, CURRENT_YEAR + 1))

CIRCUITS = {
    'Albert Park':       {'wiki': 'Melbourne_Grand_Prix_Circuit',        'country': 'Australia',    'city': 'Melbourne',       'length_km': 5.278, 'turns': 16, 'lap_record': '1:20.235 (Leclerc, 2022)',    'first_gp': 1996, 'desc': 'The Melbourne street circuit winds through Albert Park lake. Known for unpredictable results and as the traditional season opener.'},
    'Sakhir':            {'wiki': 'Bahrain_International_Circuit',       'country': 'Bahrain',      'city': 'Sakhir',          'length_km': 5.412, 'turns': 15, 'lap_record': '1:31.447 (De la Rosa, 2005)', 'first_gp': 2004, 'desc': 'Often raced at night or dusk. Hard on tyres due to abrasive tarmac. A key race early in the season.'},
    'Jeddah':            {'wiki': 'Jeddah_Street_Circuit',               'country': 'Saudi Arabia', 'city': 'Jeddah',          'length_km': 6.174, 'turns': 27, 'lap_record': '1:30.734 (Leclerc, 2022)',    'first_gp': 2021, 'desc': 'One of the fastest street circuits in the world. Nearly continuous sweeping corners at very high speed.'},
    'Suzuka':            {'wiki': 'Suzuka_International_Racing_Course',  'country': 'Japan',        'city': 'Suzuka',          'length_km': 5.807, 'turns': 18, 'lap_record': '1:30.983 (Hamilton, 2019)',   'first_gp': 1987, 'desc': 'Fan favourite with a figure-of-eight layout. Esses, Degner curves, and 130R demand total commitment.'},
    'Shanghai':          {'wiki': 'Shanghai_International_Circuit',      'country': 'China',        'city': 'Shanghai',        'length_km': 5.451, 'turns': 16, 'lap_record': '1:32.238 (Räikkönen, 2004)',  'first_gp': 2004, 'desc': 'Features a distinctive snail-shaped turn 1–2 and a very long back straight ideal for DRS battles.'},
    'Miami':             {'wiki': 'Miami_International_Autodrome',       'country': 'USA',          'city': 'Miami Gardens',   'length_km': 5.412, 'turns': 19, 'lap_record': '1:29.708 (Verstappen, 2023)', 'first_gp': 2022, 'desc': 'Built around the Hard Rock Stadium with a fake marina. High-energy atmosphere and exciting DRS zones.'},
    'Imola':             {'wiki': 'Autodromo_Enzo_e_Dino_Ferrari',       'country': 'Italy',        'city': 'Imola',           'length_km': 4.909, 'turns': 19, 'lap_record': '1:15.484 (Verstappen, 2022)', 'first_gp': 1980, 'desc': 'Steeped in history. Narrow layout rewards qualifying pace and makes overtaking very difficult. Senna\'s final race was here.'},
    'Monaco':            {'wiki': 'Circuit_de_Monaco',                   'country': 'Monaco',       'city': 'Monte Carlo',     'length_km': 3.337, 'turns': 19, 'lap_record': '1:12.909 (Leclerc, 2024)',    'first_gp': 1950, 'desc': 'The most iconic circuit in motorsport. Impossibly narrow streets, zero run-off, layout unchanged since 1929.'},
    'Catalunya':         {'wiki': 'Circuit_de_Barcelona-Catalunya',      'country': 'Spain',        'city': 'Barcelona',       'length_km': 4.657, 'turns': 16, 'lap_record': '1:18.149 (Verstappen, 2021)', 'first_gp': 1991, 'desc': 'Every team knows this circuit inside-out from pre-season testing. Very hard on rear tyres.'},
    'Montréal':          {'wiki': 'Circuit_Gilles_Villeneuve',           'country': 'Canada',       'city': 'Montreal',        'length_km': 4.361, 'turns': 14, 'lap_record': '1:13.078 (Bottas, 2019)',    'first_gp': 1978, 'desc': 'Named after Gilles Villeneuve. Features heavy braking zones and the notorious Wall of Champions.'},
    'Spielberg':         {'wiki': 'Red_Bull_Ring',                       'country': 'Austria',      'city': 'Spielberg',       'length_km': 4.318, 'turns': 10, 'lap_record': '1:05.619 (Bottas, 2020)',    'first_gp': 1970, 'desc': 'Short and fast, surrounded by Alpine scenery. High-speed corners and big elevation changes.'},
    'Silverstone':       {'wiki': 'Silverstone_Circuit',                 'country': 'UK',           'city': 'Silverstone',     'length_km': 5.891, 'turns': 18, 'lap_record': '1:27.097 (Hamilton, 2020)',  'first_gp': 1950, 'desc': 'Home of British motorsport and host of the very first World Championship race in 1950.'},
    'Budapest':          {'wiki': 'Hungaroring',                         'country': 'Hungary',      'city': 'Budapest',        'length_km': 4.381, 'turns': 14, 'lap_record': '1:16.627 (Hamilton, 2020)',  'first_gp': 1986, 'desc': 'Tight and twisty — often described as Monaco without walls. High downforce is essential.'},
    'Spa-Francorchamps': {'wiki': 'Circuit_de_Spa-Francorchamps',        'country': 'Belgium',      'city': 'Stavelot',        'length_km': 7.004, 'turns': 19, 'lap_record': '1:46.286 (Bottas, 2018)',    'first_gp': 1950, 'desc': 'Many drivers\' favourite. Eau Rouge–Raidillon, the Kemmel Straight, and Pouhon create an epic challenge.'},
    'Zandvoort':         {'wiki': 'Circuit_Zandvoort',                   'country': 'Netherlands',  'city': 'Zandvoort',       'length_km': 4.259, 'turns': 14, 'lap_record': '1:11.097 (Verstappen, 2021)', 'first_gp': 1952, 'desc': 'Back on the calendar for Verstappen\'s home fans. Famous for banked corners including a 19-degree banked hairpin.'},
    'Monza':             {'wiki': 'Autodromo_Nazionale_Monza',           'country': 'Italy',        'city': 'Monza',           'length_km': 5.793, 'turns': 11, 'lap_record': '1:21.046 (Barrichello, 2004)','first_gp': 1950, 'desc': 'The Temple of Speed. Minimal downforce setup produces the highest top speeds of the season.'},
    'Baku':              {'wiki': 'Baku_City_Circuit',                   'country': 'Azerbaijan',   'city': 'Baku',            'length_km': 6.003, 'turns': 20, 'lap_record': '1:43.009 (Leclerc, 2019)',    'first_gp': 2016, 'desc': 'Longest straight in F1 alongside the Caspian Sea. The Castle section is incredibly narrow. Safety Cars are frequent.'},
    'Marina Bay':        {'wiki': 'Marina_Bay_Street_Circuit',           'country': 'Singapore',    'city': 'Singapore',       'length_km': 5.063, 'turns': 23, 'lap_record': '1:35.867 (Sainz, 2023)',      'first_gp': 2008, 'desc': 'The original night race. Humidity, heat, and bumpy streets push drivers and cars to the absolute limit.'},
    'Austin':            {'wiki': 'Circuit_of_the_Americas',             'country': 'USA',          'city': 'Austin',          'length_km': 5.513, 'turns': 20, 'lap_record': '1:36.169 (Leclerc, 2019)',    'first_gp': 2012, 'desc': 'The only purpose-built F1 circuit in the USA. Unique anti-clockwise turn 1 and significant elevation changes.'},
    'Mexico City':       {'wiki': 'Autodromo_Hermanos_Rodriguez',        'country': 'Mexico',       'city': 'Mexico City',     'length_km': 4.304, 'turns': 17, 'lap_record': '1:17.774 (Bottas, 2021)',    'first_gp': 1963, 'desc': 'At 2,285m above sea level, thin air reduces downforce and engine power. The stadium section finale is spectacular.'},
    'São Paulo':         {'wiki': 'Autodromo_Jose_Carlos_Pace',          'country': 'Brazil',       'city': 'São Paulo',       'length_km': 4.309, 'turns': 15, 'lap_record': '1:10.540 (Räikkönen, 2004)',  'first_gp': 1973, 'desc': 'Interlagos runs anti-clockwise and always delivers drama. Weather can change rapidly mid-race.'},
    'Las Vegas':         {'wiki': 'Las_Vegas_Strip_Circuit',             'country': 'USA',          'city': 'Las Vegas',       'length_km': 6.201, 'turns': 17, 'lap_record': '1:35.490 (Leclerc, 2023)',    'first_gp': 2023, 'desc': 'Racing past casinos and hotels on the Las Vegas Strip. Cold night temperatures create interesting tyre dynamics.'},
    'Lusail':            {'wiki': 'Lusail_International_Circuit',        'country': 'Qatar',        'city': 'Lusail',          'length_km': 5.419, 'turns': 16, 'lap_record': '1:24.319 (Verstappen, 2023)', 'first_gp': 2021, 'desc': 'Originally built for MotoGP. Smooth tarmac and fast corners heavily reward aerodynamic efficiency.'},
    'Yas Marina':        {'wiki': 'Yas_Marina_Circuit',                  'country': 'UAE',          'city': 'Abu Dhabi',       'length_km': 5.281, 'turns': 16, 'lap_record': '1:26.103 (Verstappen, 2021)', 'first_gp': 2009, 'desc': 'The traditional season finale. Redesigned in 2021 with longer DRS zones. Spectacular under floodlights.'},
}

DRIVERS_2026 = [
    # McLaren-Mercedes
    {'name': 'Lando Norris',         'code': 'NOR', 'number': 1,  'team': 'McLaren',         'nationality': '🇬🇧 British',     'dob': '13 Nov 1999', 'championships': 1, 'wiki': 'Lando_Norris',                      'bio': 'Taking the #1 on his car after an incredible championship-winning campaign.'},
    {'name': 'Oscar Piastri',        'code': 'PIA', 'number': 81, 'team': 'McLaren',         'nationality': '🇦🇺 Australian',  'dob': '6 Apr 2001',  'championships': 0, 'wiki': 'Oscar_Piastri',                     'bio': 'Calm, analytical, and incredibly fast, forming a formidable duo with Norris.'},
    
    # Red Bull Racing-Red Bull Ford
    {'name': 'Max Verstappen',       'code': 'VER', 'number': 33, 'team': 'Red Bull Racing', 'nationality': '🇳🇱 Dutch',       'dob': '30 Sep 1997', 'championships': 4, 'wiki': 'Max_Verstappen',                    'bio': 'Four-time world champion. Leading Red Bull into the new Ford powertrain era.'},
    {'name': 'Isack Hadjar',         'code': 'HAD', 'number': 6,  'team': 'Red Bull Racing', 'nationality': '🇫🇷 French',      'dob': '28 Sep 2004', 'championships': 0, 'wiki': 'Isack_Hadjar',                      'bio': 'Earned his promotion to the main team after impressive feeder series performances.'},
    
    # Ferrari
    {'name': 'Charles Leclerc',      'code': 'LEC', 'number': 16, 'team': 'Ferrari',         'nationality': '🇲🇨 Monégasque',  'dob': '16 Oct 1997', 'championships': 0, 'wiki': 'Charles_Leclerc',                   'bio': 'A Ferrari prodigy and one of the fastest qualifiers on the grid.'},
    {'name': 'Lewis Hamilton',       'code': 'HAM', 'number': 44, 'team': 'Ferrari',         'nationality': '🇬🇧 British',     'dob': '7 Jan 1985',  'championships': 7, 'wiki': 'Lewis_Hamilton',                    'bio': 'The most decorated driver in F1 history chasing his eighth world title in red.'},
    
    # Mercedes
    {'name': 'George Russell',       'code': 'RUS', 'number': 63, 'team': 'Mercedes',        'nationality': '🇬🇧 British',     'dob': '15 Feb 1998', 'championships': 0, 'wiki': 'George_Russell_(racing_driver)',    'bio': 'Stepped up as the team leader at Mercedes following Hamilton’s departure.'},
    {'name': 'Kimi Antonelli',       'code': 'ANT', 'number': 12, 'team': 'Mercedes',        'nationality': '🇮🇹 Italian',     'dob': '25 Aug 2006', 'championships': 0, 'wiki': 'Andrea_Kimi_Antonelli',             'bio': 'A highly touted Mercedes junior who bypassed F3 to fast-track into F1.'},
    
    # Aston Martin Aramco-Honda
    {'name': 'Fernando Alonso',      'code': 'ALO', 'number': 14, 'team': 'Aston Martin',    'nationality': '🇪🇸 Spanish',     'dob': '29 Jul 1981', 'championships': 2, 'wiki': 'Fernando_Alonso',                   'bio': 'Two-time champion and veteran master of racecraft. Reunited with Honda engines in 2026.'},
    {'name': 'Lance Stroll',         'code': 'STR', 'number': 18, 'team': 'Aston Martin',    'nationality': '🇨🇦 Canadian',    'dob': '29 Oct 1998', 'championships': 0, 'wiki': 'Lance_Stroll',                      'bio': 'Brings immense experience to the team with flashes of brilliance in wet conditions.'},
    
    # Alpine-Mercedes
    {'name': 'Pierre Gasly',         'code': 'GAS', 'number': 10, 'team': 'Alpine',          'nationality': '🇫🇷 French',      'dob': '7 Feb 1996',  'championships': 0, 'wiki': 'Pierre_Gasly',                      'bio': 'The experienced team leader at Alpine.'},
    {'name': 'Franco Colapinto',     'code': 'COL', 'number': 43, 'team': 'Alpine',          'nationality': '🇦🇷 Argentine',   'dob': '27 May 2003', 'championships': 0, 'wiki': 'Franco_Colapinto',                  'bio': 'Secured a full-time seat at Alpine after making a huge impression as a rookie.'},
    
    # Williams-Mercedes
    {'name': 'Alexander Albon',      'code': 'ALB', 'number': 23, 'team': 'Williams',        'nationality': '🇹🇭 Thai',        'dob': '23 Mar 1996', 'championships': 0, 'wiki': 'Alexander_Albon',                   'bio': 'The anchor of the Williams rebuild. Known for his incredible tire management.'},
    {'name': 'Carlos Sainz Jr.',     'code': 'SAI', 'number': 55, 'team': 'Williams',        'nationality': '🇪🇸 Spanish',     'dob': '1 Sep 1994',  'championships': 0, 'wiki': 'Carlos_Sainz_Jr.',                  'bio': 'A highly intelligent race winner pushing Williams back to the front of the grid.'},
    
    # Racing Bulls-Red Bull Ford
    {'name': 'Liam Lawson',          'code': 'LAW', 'number': 30, 'team': 'Racing Bulls',    'nationality': '🇳🇿 New Zealander','dob': '11 Feb 2002', 'championships': 0, 'wiki': 'Liam_Lawson',                     'bio': 'Known for his adaptability and cool head under pressure.'},
    {'name': 'Arvid Lindblad',       'code': 'LIN', 'number': 41, 'team': 'Racing Bulls',    'nationality': '🇬🇧 British',     'dob': '8 Aug 2007',  'championships': 0, 'wiki': 'Arvid_Lindblad',                    'bio': 'Red Bull junior prospect who rapidly ascended the feeder series ladder.'},
    
    # Haas-Ferrari
    {'name': 'Esteban Ocon',         'code': 'OCO', 'number': 31, 'team': 'Haas',            'nationality': '🇫🇷 French',      'dob': '17 Sep 1996', 'championships': 0, 'wiki': 'Esteban_Ocon',                      'bio': 'A proven race winner who moved to Haas to lead their project.'},
    {'name': 'Oliver Bearman',       'code': 'BEA', 'number': 87, 'team': 'Haas',            'nationality': '🇬🇧 British',     'dob': '8 May 2005',  'championships': 0, 'wiki': 'Oliver_Bearman',                    'bio': 'Ferrari junior highly rated for his raw pace and spectacular substitute performances.'},
    
    # Audi
    {'name': 'Nico Hülkenberg',      'code': 'HUL', 'number': 27, 'team': 'Audi',            'nationality': '🇩🇪 German',      'dob': '19 Aug 1987', 'championships': 0, 'wiki': 'Nico_Hülkenberg',                   'bio': 'The experienced German chosen to lead Audi’s historic entry into Formula 1.'},
    {'name': 'Gabriel Bortoleto',    'code': 'BOR', 'number': 5,  'team': 'Audi',            'nationality': '🇧🇷 Brazilian',   'dob': '14 Oct 2004', 'championships': 0, 'wiki': 'Gabriel_Bortoleto',                 'bio': 'Brought in to be the young foundation of the new Audi works team.'},
    
    # Cadillac-Ferrari
    {'name': 'Sergio Pérez',         'code': 'PER', 'number': 11, 'team': 'Cadillac',        'nationality': '🇲🇽 Mexican',     'dob': '26 Jan 1990', 'championships': 0, 'wiki': 'Sergio_Pérez',                      'bio': 'Veteran driver bringing his vast experience to the new American Cadillac team.'},
    {'name': 'Valtteri Bottas',      'code': 'BOT', 'number': 77, 'team': 'Cadillac',        'nationality': '🇫🇮 Finnish',     'dob': '28 Aug 1989', 'championships': 0, 'wiki': 'Valtteri_Bottas',                   'bio': 'Experienced multiple race winner joining the new Cadillac project.'},
]

DRIVER_MAP = {d['code']: d for d in DRIVERS_2026}

CONSTRUCTORS_2026 = [
    {'name': 'McLaren',         'base': 'Woking, UK',           'founded': 1966, 'championships': 8,  'color': '#FF8000', 'desc': 'Powered by Mercedes engines. Entering 2026 with a championship-winning pedigree.'},
    {'name': 'Red Bull Racing', 'base': 'Milton Keynes, UK',    'founded': 2005, 'championships': 6,  'color': '#3671C6', 'desc': 'Entering a new era in 2026 manufacturing their own Red Bull Ford powertrains.'},
    {'name': 'Ferrari',         'base': 'Maranello, Italy',     'founded': 1950, 'championships': 16, 'color': '#E8002D', 'desc': 'The most storied team in F1 history. Boasts a massive driver lineup of Hamilton and Leclerc.'},
    {'name': 'Mercedes',        'base': 'Brackley, UK',         'founded': 1954, 'championships': 8,  'color': '#27F4D2', 'desc': 'Eight-time champions looking to dominate the 2026 engine regulations.'},
    {'name': 'Aston Martin',    'base': 'Silverstone, UK',      'founded': 2021, 'championships': 0,  'color': '#229971', 'desc': 'Now the official Honda works team for 2026. Designed by Adrian Newey.'},
    {'name': 'Alpine',          'base': 'Enstone, UK',          'founded': 2021, 'championships': 0,  'color': '#FF87B2', 'desc': 'Transitioned from a works team to a customer Mercedes engine model for the 2026 regulations.'},
    {'name': 'Williams',        'base': 'Grove, UK',            'founded': 1977, 'championships': 7,  'color': '#64C4FF', 'desc': 'One of F1\'s legacy teams. Continues its rebuilding phase with a highly experienced driver pairing.'},
    {'name': 'Racing Bulls',    'base': 'Faenza, Italy',        'founded': 1985, 'championships': 0,  'color': '#6692FF', 'desc': 'Red Bull\'s sister team. Powered by the new Red Bull Ford powertrains.'},
    {'name': 'Haas',            'base': 'Kannapolis, USA',      'founded': 2016, 'championships': 0,  'color': '#FFFFFF', 'desc': 'The American squad relying on a close technical partnership with Ferrari.'},
    {'name': 'Audi',            'base': 'Hinwil, Switzerland',  'founded': 2026, 'championships': 0,  'color': '#F50537', 'desc': 'The German automotive giant officially enters F1 as a works team in 2026.'},
    {'name': 'Cadillac',        'base': 'Detroit, USA',         'founded': 2026, 'championships': 0,  'color': '#000000', 'desc': 'The 11th team on the grid, backed by General Motors and running Ferrari customer engines.'},
]

LEGENDS = [
    {'name': 'Ayrton Senna',        'years': '1984–1994',            'championships': 3, 'nationality': '🇧🇷 Brazilian',  'wins': 41, 'wiki': 'Ayrton_Senna',        'quote': 'You commit, you give everything — that is the only way.', 'desc': 'Widely regarded as the greatest driver of all time. His rivalry with Alain Prost defined an era. Tragically killed at the 1994 San Marino Grand Prix at Imola.'},
    {'name': 'Michael Schumacher',  'years': '1991–2006, 2010–2012', 'championships': 7, 'nationality': '🇩🇪 German',     'wins': 91, 'wiki': 'Michael_Schumacher',  'quote': 'Once something is a passion, the motivation is there.', 'desc': 'Seven world championships, 91 wins. Dominated F1 with Ferrari from 2000–2004. His records stood for over a decade before Hamilton equalled them.'},
    {'name': 'Juan Manuel Fangio',  'years': '1950–1958',            'championships': 5, 'nationality': '🇦🇷 Argentine',  'wins': 24, 'wiki': 'Juan_Manuel_Fangio',  'quote': 'You must always go on in spite of something.', 'desc': 'The original master. Five championships across four different constructor teams. His win rate of 46.5% has never been matched.'},
    {'name': 'Jim Clark',           'years': '1960–1968',            'championships': 2, 'nationality': '🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scottish',   'wins': 25, 'wiki': 'Jim_Clark',           'quote': 'It is difficult to say what is impossible.', 'desc': 'Considered by many to be the most naturally gifted driver in history. Won the 1965 championship and the Indianapolis 500 in the same year.'},
    {'name': 'Alain Prost',         'years': '1980–1991, 1993',      'championships': 4, 'nationality': '🇫🇷 French',     'wins': 51, 'wiki': 'Alain_Prost',         'quote': 'The victory is always worth the effort.', 'desc': 'The "Professor" — a calculating, intelligent driver who could pace a race perfectly. His rivalry with Senna remains the sport\'s most famous.'},
    {'name': 'Niki Lauda',          'years': '1971–1979, 1982–1985', 'championships': 3, 'nationality': '🇦🇹 Austrian',   'wins': 25, 'wiki': 'Niki_Lauda',          'quote': 'I have no idols. I admire work, dedication and competence.', 'desc': 'Survived a horrific crash at the 1976 Nürburgring, returning just six weeks later with his face still healing. One of sport\'s greatest stories of courage.'},
]

HISTORY_ERAS = [
    {'era': '1950s – The beginning',            'years': '1950–1959',    'desc': 'The FIA World Championship began in 1950 at Silverstone. Juan Manuel Fangio dominated, winning five of the decade\'s ten championships. Cars were front-engined, often derived from pre-war designs.'},
    {'era': '1960s – The rear-engine revolution','years': '1960–1969',   'desc': 'Cooper and Lotus pioneered rear-engined cars, transforming performance. Jim Clark and Jack Brabham were the stars. Safety was not a priority and the mortality rate among drivers was tragically high.'},
    {'era': '1970s – Ground effect & politics',  'years': '1970–1979',   'desc': 'Lotus introduced ground-effect aerodynamics, producing huge downforce. Niki Lauda\'s crash and comeback in 1976 remains one of sport\'s most extraordinary stories.'},
    {'era': '1980s – The turbo wars',            'years': '1980–1989',   'desc': 'Turbocharged engines producing over 1,400 hp in qualifying trim defined the decade. The Senna–Prost rivalry began at McLaren. Turbos were eventually banned in 1989.'},
    {'era': '1990s – Senna, Schumacher & safety','years': '1990–1999',   'desc': 'Senna\'s death in 1994 triggered a safety revolution led by the FIA. Schumacher rose to dominance with Benetton and then Ferrari. The decade ended with a German dynasty forming.'},
    {'era': '2000s – The Schumacher era',        'years': '2000–2009',   'desc': 'Schumacher won five consecutive championships from 2000–2004 with Ferrari. Renault fought back with Alonso. A young Lewis Hamilton appeared in 2007 and nearly won the title in his debut season.'},
    {'era': '2010s – The hybrid era',            'years': '2010–2019',   'desc': 'Red Bull dominated 2010–2013 with Vettel. Mercedes\' hybrid power unit introduced in 2014 was transformative — they won seven consecutive constructors\' championships.'},
    {'era': '2020s – A new generation',          'years': '2020–present','desc': 'Verstappen broke Hamilton\'s dominance in a controversial 2021 finale, then dominated 2022–2023. McLaren and Ferrari closed the gap in 2024, with 2025–2026 seeing the closest competition in years.'},
]

GLOSSARY = [
    ('DRS',                 'Drag Reduction System. Opens a flap in the rear wing to reduce drag on straights, allowing the following car to attack.'),
    ('Undercut',            'A strategy where a driver pits earlier than the rival to gain time on fresher tyres, emerging ahead.'),
    ('Overcut',             'Staying out longer on old tyres hoping the rival\'s in-lap plus stop time is slower.'),
    ('VSC',                 'Virtual Safety Car. All cars must reduce speed significantly but do not need to form a queue behind a physical car.'),
    ('Safety Car',          'A physical pace car deployed onto the circuit. All cars must queue up behind it and cannot overtake.'),
    ('Parc Fermé',          'A set of rules restricting changes to the car between qualifying and the race. Allows only limited setup adjustments.'),
    ('Graining',            'Small pieces of rubber tear from the tyre surface, reducing grip temporarily before wearing away.'),
    ('Blistering',          'Heat causes the tyre rubber to form blisters, causing permanent degradation and loss of performance.'),
    ('Ground effect',       'The floor of the car creates a low-pressure area that sucks the car to the track, generating downforce without extra drag.'),
    ('MGU-K / MGU-H',       'Motor Generator Units (Kinetic/Heat). Part of the hybrid power unit recovering energy from braking and exhaust gases.'),
    ('Marbles',             'Rubber debris that builds up off the racing line. Driving over marbles is extremely slippery and reduces lap times significantly.'),
    ('Snap oversteer',      'When the rear of the car suddenly slides out, requiring a quick steering correction. Often causes spins if not caught.'),
    ('Tifosi',              'The passionate Italian fans, particularly Ferrari supporters. Present in huge numbers at Monza and Imola.'),
    ('Quali mode',          'An engine mode used only in qualifying for maximum power output — not sustainable over race distance.'),
]

QUIZ_QUESTIONS = [
    {'q': 'Which driver holds the record for most Formula 1 World Championships?',
     'options': ['Ayrton Senna', 'Michael Schumacher', 'Lewis Hamilton', 'Juan Manuel Fangio'],
     'answer': 'Michael Schumacher',
     'fact': 'Schumacher and Hamilton are tied at seven championships each — the joint record. Schumacher won his between 1994 and 2004, Hamilton between 2008 and 2020.'},
    {'q': 'In which year did the Formula 1 World Championship first take place?',
     'options': ['1948', '1950', '1952', '1955'],
     'answer': '1950',
     'fact': 'The first F1 World Championship race was held at Silverstone on 13 May 1950. Giuseppe Farina won both the race and the championship that year.'},
    {'q': 'What does DRS stand for?',
     'options': ['Drag Reduction System', 'Driver Racing Strategy', 'Dynamic Rear Spoiler', 'Direct Response System'],
     'answer': 'Drag Reduction System',
     'fact': 'DRS was introduced in 2011 to aid overtaking. It opens a flap in the rear wing, reducing drag and increasing top speed by roughly 10–15 km/h.'},
    {'q': 'Which circuit is known as "The Temple of Speed"?',
     'options': ['Spa-Francorchamps', 'Silverstone', 'Monza', 'Suzuka'],
     'answer': 'Monza',
     'fact': 'Monza in Italy is one of the fastest circuits on the calendar. Its long straights and low-downforce setup make engine performance crucial.'},
    {'q': 'Which constructor has won the most Formula 1 World Championships?',
     'options': ['Red Bull Racing', 'McLaren', 'Williams', 'Ferrari'],
     'answer': 'Ferrari',
     'fact': 'Ferrari has won 16 Constructors\' Championships, making them the most successful team in F1 history. They first won the title in 1961.'},
    {'q': 'What does "undercut" mean in F1 strategy?',
     'options': ['Driving below the racing line to pass', 'Pitting earlier than a rival to gain track position on fresh tyres', 'Cutting a corner to gain time', 'Using a softer tyre compound at race start'],
     'answer': 'Pitting earlier than a rival to gain track position on fresh tyres',
     'fact': 'The undercut works when the time gained on fresh tyres outweighs the time lost in the pit stop itself — a key strategic weapon in modern F1.'},
    {'q': 'At which circuit did Ayrton Senna die during the 1994 San Marino Grand Prix?',
     'options': ['Monaco', 'Monza', 'Imola', 'Hockenheim'],
     'answer': 'Imola',
     'fact': 'Senna died at the Autodromo Enzo e Dino Ferrari in Imola, Italy, on 1 May 1994. His death prompted sweeping safety reforms that have saved countless lives.'},
    {'q': 'Which team introduced ground-effect aerodynamics to F1 in the late 1970s?',
     'options': ['Ferrari', 'McLaren', 'Lotus', 'Tyrrell'],
     'answer': 'Lotus',
     'fact': 'Colin Chapman pioneered ground-effect aerodynamics with the Lotus 78 in 1977 and the revolutionary Lotus 79 in 1978, which dominated that season.'},
    {'q': 'Who was the youngest driver to win a Formula 1 Grand Prix?',
     'options': ['Sebastian Vettel', 'Max Verstappen', 'Lance Stroll', 'Lando Norris'],
     'answer': 'Max Verstappen',
     'fact': 'Verstappen was 18 years and 228 days old when he won the 2016 Spanish Grand Prix — his first race for Red Bull after being promoted from Toro Rosso.'},
    {'q': 'What colour flag signals the end of a race in F1?',
     'options': ['Yellow flag', 'Blue flag', 'Chequered flag', 'Red flag'],
     'answer': 'Chequered flag',
     'fact': 'The chequered (black and white squares) flag has signalled the end of races since the early days of motorsport. A red flag stops the session entirely.'},
]