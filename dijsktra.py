# Zadání: Dijkstrův algoritmus pro hledání nejkratší cesty v mapě reprezentované Unicode znaky.
# Každý znak má přiřazenou cenu pohybu, a algoritmus musí najít nejlevnější cestu z bodu A do bodu B.
# Implementace by měla být efektivní a správně zpracovávat různé typy terénu, včetně překážek a různých nákladů na pohyb.

# Mapa se zadává jako jeden string s celou mapou, kde každý řádek je oddělen novým řádkem (\n). Například:
# map = """✅🌲🌲🌲🌲🌲🌲🌲
# 🚗🚗🚗🚗🌱🌱🌱🌱🌱🌱"""

# Výchozí bod je označen znakem "✅" a cílový bod je označen znakem "🚩".
# Ostatní znaky reprezentují různé typy terénu s různými náklady na pohyb, které jsou definovány v mapě znaků.
# Je třeba implementovat metody pro parsování mapy, výpočet nejkratší cesty pomocí Dijkstraova algoritmu a vytvoření výsledné cesty a jejího nákladu.  

# Maximalní vzdálenost pro neprocházetelné terény
MAXDIST = float('inf')


chars = {"🌱" : 5, #grass 
         "🚂" : 2, #railway
         "🚗" : 1, #highway                  
         "💦" : MAXDIST, #water
         "🌲" : 6,   #forest
         "⚪" : 1,   #empty
         "⬛" : MAXDIST,   #wall
         "🚩" : 0,    #finish
         "✅" : 0     #start
         }
"""Mapa znaků a jejich odpovídající náklady na pohyb"""

# Třída pro reprezentaci mapy a implementaci Dijkstraova algoritmu
class UnicodeMap:
    def __init__(self):
        """Inicializace třídy"""
        self.Map = []
        """mapa implementovaná jako 2D pole"""
        self.Start: (int, int) 
        """pozice startu"""
        self.Finish: (int, int)
        """pozice finiše"""
        self.Dist = []
        """Vzdálenosti od startu"""
        self.Prev = []
        """Odkaď jsme na políčko přišli"""


    def dijkstra(self):
        """Metoda pro výpočet nejkratší cesty pomocí Dijkstraova algoritmu

        # Nemá žádné parametry, protože používá atributy třídy pro uložení stavu algoritmu"""
        """množina vrcholů, kam už známe nejkratší cestu. Pole tuplů (souřadnice aktuálního vrcholu, předcházející vrchol, vzdálenost z počátku)"""

        """aktuální vzdálenosti všech vrcholů od počátku"""
        #nastavíme vzdálenosti od počátku
        radky = len(self.Map)
        sloupce = len(self.Map[0]) #počet řádků a sloupců
        
        self.Dist = [
            [MAXDIST for _ in range(sloupce)]
            for _ in range(radky)
        ] #na začátku jsme do žádného vrcholu cestu nenašli

        self.Prev = [
            [None for _ in range(sloupce)]
            for _ in range(radky)
        ] 

        
        Q = [] #prioritní fronta

        sy, sx = self.Start #souřadnice startu

        self.Dist[sy][sx] = 0 #cestu do startu 

        Q.append((0, self.Start))
        directions = [
            (-1, 0), #nahoru
            (0, 1), #doprava
            (1, 0), #dolů
            (0, -1) #doleva
        ]
        """slovník pro převod souřadnic (0 nahoru, dál ve směru hod. ručiček)"""

        while Q:
            # ruční hledání minima
            min_i = 0
            for i in range(len(Q)):
                if Q[i][0] < Q[min_i][0]:
                    min_i = i
            current_dist, (y, x) = Q.pop(min_i) #vemem a vyhodíme nejmenší prvek z fronty

            if (y, x) == self.Finish: #jsme v cíli
                return

            for dy, dx in directions:
                ny = y + dy
                nx = x + dx

                cost = self.Map[ny][nx]

                if cost is None or cost == MAXDIST:
                    continue

                new_dist = current_dist + cost

                if new_dist < self.Dist[ny][nx]:

                    self.Dist[ny][nx] = new_dist
                    self.Prev[ny][nx] = (y, x)

                    Q.append((new_dist, (ny, nx)))
                


    def make_solution(self):
        """# Metoda pro vytvoření výsledné cesty a jejího nákladu
        # Měla by vrátit tuple obsahující celkovou vzdálenost a seznam (list) bodů na cestě od startu k cíli,
        včetně startu a cíle. Například: (10, [(0,0), (1,0), (1,1), (2,1)])"""
        fy, fx = self.Finish

        distance = self.Dist[fy][fx]

        if distance == MAXDIST:
            return MAXDIST, []

        path = []

        current = self.Finish

        while current is not None:

            y, x = current

            # odstranění okrajového posunu
            path.append((x - 1, y - 1))

            current = self.Prev[y][x]

        path.reverse()

        return (distance, path)
   
    def parse_map(self, map:str):
        """ Metoda pro parsování mapy ze stringu a vytvoření grafu pro algoritmus
        # Vstupem je string obsahující mapu, kde každý řádek je oddělen novým řádkem (\n).
        # Metoda by měla také najít start a cíl a uložit je do atributů třídy.
        # Mapu je dobré uložit jako 2D list, kde každý prvek je náklad na pohyb do dané pozice,
        což usnadní implementaci Dijkstraova algoritmu.    
        # V případě, že mapa neobsahuje start nebo cíl, by měla metoda vyhodit výjimku (raise ValueError).
        # !!! Mapa má po okrajích hodnoty None pro zamezení chyb !!!"""
        self.Map = []
        mapa: list = map.split("\n")
        foundstart, foundfinish = False, False
        radek0 = [None] * (len(mapa[0]) + 2)
        self.Map.append(radek0)
        for i in range(len(mapa)):
            radek = []
            radek.append(None)
            for j in range(len(mapa[i])):
                radek.append(chars[mapa[i][j]])
                if mapa[i][j] == "✅" and not foundstart:
                    self.Start = (i+1, j+1)
                    foundstart = True
                elif mapa[i][j] == "🚩" and not foundfinish:
                    self.Finish = (i+1, j+1)
                    foundfinish = True
            radek.append(None)
            self.Map.append(radek)
        self.Map.append(radek0)
        if (not foundstart) or (not foundfinish):
            raise ValueError("Chybí mi počáteční nebo koncová pozice")
        





# KONEC IMPLEMENTACE TŘÍDY ZDE

# NÁSLEDUJE TESTOVÁNÍ ALGORITMU NA UKÁZKOVÝCH MAPÁCH

# funkce, která vypíše mapu s vyznačenou cestou, pro lepší vizualizaci výsledku
def print_map(map:str, path:list):
    maplines = map.splitlines()
    for y in range(len(maplines)):
        for x in range(len(maplines[0])):
            if (x,y) in path:
                print('\33[45m', end="")
            else:
                print('\33[0m', end="")
            print(maplines[y][x], end="")
        print('\33[0m')

# Ukázkové mapy pro testování algoritmu
map1 = """✅🌲🌲🌲🌲🌲🌲🌲🌲🌲
🚗🚗🚗🚗🌱🌱🌱🌱🌱🌱
🚗🌱🌱🌱🌱🌱🌲🌲🌲🚂
🚗🚗🚗💦💦💦💦🌱🌱🚂
🌱🌱🚗💦💦💦💦🌱🌱🚂
🌱🌱🚗💦🌱🌱🌱🌲🌲🌱
🌱🌱🌱🌱🌱🌱🌱🌱🌱🚩"""

# chybná mapa, není zde začátek.
map1_error = """🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲
🚗🚗🚗🚗🌱🌱🌱🌱🌱🌱
🚗🌱🌱🌱🌱🌱🌲🌲🌲🚂
🚗🚗🚗💦💦💦💦🌱🌱🚂
🌱🌱🚗💦💦💦💦🌱🌱🚂
🌱🌱🚗💦🌱🌱🌱🌲🌲🌱
🌱🌱🌱🌱🌱🌱🌱🌱🌱🚩"""

# další chybná mapa, není zde cíl.
map1_error2 = """✅🌲🌲🌲🌲🌲🌲🌲🌲🌲
🚗🚗🚗🚗🌱🌱🌱🌱🌱🌱
🚗🌱🌱🌱🌱🌱🌲🌲🌲🚂
🚗🚗🚗💦💦💦💦🌱🌱🚂
🌱🌱🚗💦💦💦💦🌱🌱🚂
🌱🌱🚗💦🌱🌱🌱🌲🌲🌱
🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱"""

# Další mapa pro testování algoritmu
map2 = """✅🚂🌱💦🚗💦💦🌱🚂🌱🌱💦🌱🌱🌱🌱🌱🌱🌱🌱🌱🚗🌱🚂🌱🚗🌱🚂🌲🌱
🚂🚂🚂🌱🚗🌱🌱🌱🌲💦🌱🌱🌱🌲🌱🌱🌱🌲🌱🌱🚗🌱🌱🚂🌱🚗🌱🌱🌲🌱
🌱🚂🌱🌱🚗🌱🌱🚗💦💦🌱🌱🌱🌲🌲🌲🌲🌱🌱🚗🚗🌱🌱🚂🌱🚗🚂🌲🌱🌱
🌱🚂💦🌱🌱🌱🌱🌱🌱🌱💦🌱🌲🌲🌲🌲🌱🌱🚗🌱🚗🌱🌱🚂🌱🌱🌱🌲🌱🌱
🌱🚂💦🚗🌱💦🌱🚂🌱🌱💦🌱🌲🌲🌲🌱🌱🚗🌱🌱🌱🌱🌱🚂🌱🚂🌲🌱🌱🌱
🌱🌱🌱🌱🚂💦🌱🌲💦🌱🌱🌱🌲🌱🌱🌱🚗🌱🌲🌱🌱🌱🌱🚂🌱🌲🚂🌱🌲🌱
🌱🌱🌱🌱🌲🌱🚗🌲💦🌱🌱🌱🌱🌱🌱🚗🌲🌲🌲🌱🌱🌱🌱🚂🚂🌲🌱🌲🌲🌱
🌱🌱🌱🌱💦🌱🌱💦🌱🌱🌱🌱🌱🌱🚗🌱🌲🌲🌲💦💦💦💦🚂🌲🌱🌱🌲🌱🌱
🌱🌱🌱🌱🌱🌱🌱💦🌱💦🌱🌱🌱🚗🌱🌱🌲🌲🌲🚂🌱🌱🌱🌱🌲🌱🌲🌲🌱🌱
🌱🌱🌱🌱🌱🌱🚂💦🌱🌱🌱🌱🌱🌱🌱🌱🌲🌲🌱🚂🌱🌱🌱🚂🌲🌱🌲🌱🌱🚗
🌱🌱🚗🚂💦🌱🌲🌲🌲🌲🌲🌲🌲🌲💦💦🌲🌲🌱🚂🌱🌱🌱🌲🌱🌱🌲🌱🚗🌱
🌱🌱🌱🌱🌱🚗🌲🌱🌱🌱🌱🌱🌱💦💦💦🌲🌱🚂🌱🌱🌱🌱🌲🌱🌲🌱🌱🌱🌱
🌱🌱🌱🌱🌱🌱🌲🌱🌱🌲🌱🌱🌱💦💦💦🌱🚂🌱🌱🌱🌱🚂🌲🌱🌲🌱🚗🌱🌱
🌱🌱🌱🌱🌱🌱💦🌱💦🌱🌱🌱💦💦🌱💦🌱🌱🌱🌱🌱🌱🌲🌱🌱🚗🌱🌱🌱🌱
🌱🚗🌱🌱🌱🚂💦🌱🌱🌱🌱🌱💦🌱🌱🚂💦🌱🌱🌱🌱🌱🌲🌱🚗🚗🚗🌱🌱🌱
🌱🌱🌱💦🚗🌲🌱🌱🌱🌱🌱🌱💦🌱🚂💦💦🌱🌱🌱🌱🌱🌱🌱🚗🚗🌱🌱🌱🌱
🌱🌱🚂💦🌱🌲🌱🌱🚂🌱🌱💦🌱🚂🌱🌱💦🌱🌱🚗🌱🌱🌱🌱🌱🚗🌱🌱🌱🌱
🚗🌱🌱🌱🌱💦💦💦💦💦💦💦🌱🌱🚗🌱💦🌱🚗🌱🌱🌱🌱🚗🌱🌱🌱🌱🌱🚂
🚂🌱🌱🌱🚂💦🌱🌱🌱💦🌱🌱🚂🚗🚗🚗💦🚗🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🚂🌱
🚂🌱💦🚗🌲💦🌱🌱🌱🌱🌱🌱🌱🌱🚗🚗🚗🌱🌱🌱🌱🌱🌱🌱🚗🚩🌱🚂🌱🌱
🚂🌱💦🚗💦🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🚗🌱🌱🌱🌱🚗🌱🚗🌱🚗🌱🌱🌱🌱🌱"""

# Bludiště pro testování algoritmu
maze1 = """⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
✅⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛
⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛
⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛
⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛
⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛
⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛
⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛
⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛
⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛
⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛
⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛
⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛
⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛
⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛
⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛
⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛
⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛
⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛
⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛
⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛
⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛
⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛
⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛
⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛
⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛
⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛
⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛
⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪🚩
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"""

# Další bludiště pro testování
maze2 = """⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
✅⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛
⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛
⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛
⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛
⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛
⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛
⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛
⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛
⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛
⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛
⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⬛⬛
⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛
⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⚪⬛⬛⬛⚪⬛⚪⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⚪⬛⬛⬛⬛⬛⚪⬛
⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⬛⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⚪⚪⚪⚪⬛⚪⬛⚪⚪⚪⚪⚪⚪⚪⚪⚪🚩
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"""


# Testování řešení
dijk = UnicodeMap()
dijk.parse_map(map1)
dijk.dijkstra()
dist, sol = dijk.make_solution()
print(f"Distance: {dist}")
print_map(map1, sol)
assert dist == 42

# Testování chybná mapa, není start nebo cíl
try:
    dijk.parse_map(map1_error)
    dijk.dijkstra()
    dist, sol = dijk.make_solution()
    print(f"Distance: {dist}")
    print_map(map1_error, sol)
except ValueError as e:
    print(f"Error: {e}")

try:
    dijk.parse_map(map1_error2)
    dijk.dijkstra()
    dist, sol = dijk.make_solution()
    print(f"Distance: {dist}")
    print_map(map1_error2, sol)
except ValueError as e:
    print(f"Error: {e}")

# Testování dalšího bludiště
dijk2 = UnicodeMap()
dijk2.parse_map(map2)
dijk2.dijkstra()
dist, sol = dijk2.make_solution()
print(f"Distance: {dist}")
print_map(map2, sol)
assert dist == 162

maze = UnicodeMap()
maze.parse_map(maze2)
maze.dijkstra()
dist, sol = maze.make_solution()
print(f"Distance: {dist}")
print_map(maze2, sol)
assert dist == 73

maze.parse_map(maze1)
maze.dijkstra()
dist, sol = maze.make_solution()
print(f"Distance: {dist}")
print_map(maze1, sol)
assert dist == 137
