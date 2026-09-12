# 🧠 Useful Algorithms

Sbírka algoritmů a datových struktur v Pythonu určená hlavně jako **pomoc při přípravě na algoritmické zkoušky**.

Nečekej knihovnu, kterou nainstaluješ přes `pip`. Tohle repo je spíš **krabička s nářadím**: když potřebuješ rychle najít implementaci spojového seznamu, zásobníku, fronty, BST nebo sortu, otevřeš správný soubor a máš před sebou funkční kostru.

> 💡 Doporučení: nekopíruj algoritmy naslepo. U zkoušky je mnohem užitečnější vědět **proč fungují a kterou část případně upravit**.

---

## 📦 Co je v repozitáři

```text
useful_algorithms/
├── BinarySearchTreePA.py
├── LinkedList.py
├── Stack.py
├── sort.py
└── README.md
```

### Rychlá mapa

| Soubor | Co tam hledat |
|---|---|
| `sort.py` | Selection sort, insertion sort, bubble sort, shaker sort, quicksort |
| `LinkedList.py` | Jednosměrný spojový seznam, iterátory, mazání, hledání, sortování |
| `Stack.py` | Stack přes linked list, stack přes Python `list`, queue |
| `BinarySearchTreePA.py` | BST, hledání, vkládání, průchody stromem, hloubka, minimum, kopie, vyvážený strom |

---

# 🚀 Jak to použít

Repo si můžeš stáhnout:

```bash
git clone https://github.com/heraya21/useful_algorithms.git
cd useful_algorithms
```

Pro aktuální verzi je nejbezpečnější použít **Python 3.10 až 3.12**.

```bash
python --version
```

`sort.py` momentálně obsahuje import z `pytest`, takže pokud dostaneš:

```text
ModuleNotFoundError: No module named '_pytest'
```

stačí:

```bash
python -m pip install pytest
```

Nebo můžeš ze `sort.py` odstranit tento nepotřebný import:

```python
from _pytest.monkeypatch import K
```

### Python 3.13+

V `Stack.py` je momentálně:

```python
from cgi import test
```

Modul `cgi` už v Pythonu 3.13 není. Tento import se v implementaci stacku nepoužívá, takže ho můžeš jednoduše odstranit.

---

# ⚡ Co použít podle zadání?

Když u zkoušky vidíš něco jako:

| Zadání / problém | Pravděpodobně chceš |
|---|---|
| „poslední vložený prvek zpracuj jako první“ | **Stack** |
| závorky, undo, DFS | **Stack** |
| „první vložený prvek zpracuj jako první“ | **Queue** |
| BFS, průchod po úrovních | **Queue** |
| často přidávám/mažu na začátku | **Linked List** |
| hledání + vkládání podle velikosti | **BST** |
| vypsat BST vzestupně | **inorder traversal** |
| klasicky seřadit pole | **Quick sort** |
| jednoduchý sort, který musíš umět vysvětlit | **Selection / Insertion sort** |
| skoro seřazená data | **Insertion sort** |
| k-tý nejmenší prvek | **Hoare / Quickselect**, ale v repu zatím není hotový |

---

# 🔢 Sorting

Soubor:

```python
sort.py
```

Import například:

```python
from sort import quick_sort

a = [5, 2, 8, 1, 3]

print(quick_sort(a))
# [1, 2, 3, 5, 8]
```

Implementované sorty vytvářejí kopii vstupního pole, takže původní list typicky zůstane beze změny:

```python
a = [3, 1, 2]

b = quick_sort(a)

print(a)
# [3, 1, 2]

print(b)
# [1, 2, 3]
```

---

## ✅ Selection sort

```python
from sort import selection_sort

a = selection_sort([5, 1, 4, 2])
```

Princip:

1. najdi nejmenší prvek,
2. dej ho na začátek,
3. pokračuj se zbytkem pole.

Složitost:

```text
čas:    O(n²)
paměť:  O(1) samotný algoritmus
```

Dobré hlavně na pochopení principu řazení. Na velká data nechceš.

---

## ✅ Insertion sort

```python
from sort import insertion_sort

a = insertion_sort([5, 1, 4, 2])
```

Princip:

Postupně buduješ seřazenou část pole a každý nový prvek vložíš na správné místo.

```text
[2, 5, 7] + [3]
     ↓
[2, 3, 5, 7]
```

Složitost:

```text
nejhorší případ: O(n²)
```

Hodí se hlavně pro malá nebo skoro seřazená pole.

---

## ✅ Bubble sort

```python
from sort import bubble_sort

a = bubble_sort([5, 1, 4, 2])
```

Porovnává sousední prvky a prohazuje je:

```text
5 1 4 2
↓
1 5 4 2
↓
1 4 5 2
↓
1 4 2 5
```

```text
O(n²)
```

Jednoduchý na vysvětlení, pomalý na větších datech.

---

## ✅ Shaker sort

```python
from sort import shaker_sort

a = shaker_sort([5, 1, 4, 2])
```

Varianta bubble sortu, která prochází pole v obou směrech.

```text
→ → → →
← ← ← ←
```

Pořád počítej přibližně s:

```text
O(n²)
```

---

## ✅ Quick sort

```python
from sort import quick_sort

a = quick_sort([5, 1, 4, 2, 8, 3])
```

V repu je rekurzivní implementace s partition funkcí `_rozdel()`.

Myšlenka:

```text
          pivot
            ↓
[menší prvky] pivot [větší prvky]
      ↓                 ↓
  quicksort          quicksort
```

Složitost:

```text
průměrně: O(n log n)
nejhůře:  O(n²)
```

Pokud potřebuješ u zkoušky jeden „opravdový“ sort, **quicksort je dobré místo, kde začít**.

---

## ⚠️ Zatím nedokončené sorty

Tyto funkce v `sort.py` existují, ale momentálně obsahují pouze `...`:

```python
binary_insertion_sort()
shell_sort()
merge_sort()
heap_sort()
hoare_algorithm()
radix_sort()
```

Takže například:

```python
from sort import merge_sort
```

sice může existovat, ale samotný algoritmus zatím **není implementovaný**.

> ⚠️ Před zkouškou si vždy zkontroluj, jestli funkce, kterou chceš použít, opravdu obsahuje implementaci a ne jen `...`.

---

# 🔗 Linked List

Soubor:

```python
LinkedList.py
```

Jedná se o **jednosměrný spojový seznam** používající sentinel `endnode`.

Zjednodušeně:

```text
head
 ↓
[10] -> [20] -> [30] -> [endnode]
```

`endnode` označuje konec seznamu a neobsahuje normální uživatelský prvek.

---

## Základ

```python
from LinkedList import LinkedList

lst = LinkedList()

lst.append(10)
lst.append(20)
lst.append(30)

print(lst)
```

Přidání na začátek:

```python
lst.insert_at_beginning(5)
```

Výsledek:

```text
5 -> 10 -> 20 -> 30
```

---

## Hledání

```python
node = lst.find(20)

if node is not None:
    print(node.data)
```

Linked list nemá výhodu binárního vyhledávání.

Musíš jít postupně:

```text
head -> node -> node -> node -> ...
```

Proto:

```text
find: O(n)
```

---

## První prvek

```python
value = lst.first()
```

```text
O(1)
```

---

## Poslední prvek

```python
value = lst.last()
```

Protože jde o jednosměrný seznam, musíš dojít od začátku až na konec:

```text
O(n)
```

---

## Mazání prvního prvku

```python
value = lst.remove_first()
```

```text
O(1)
```

Stačí posunout `head`.

---

## Mazání posledního prvku

```python
value = lst.remove_last()
```

```text
O(n)
```

Musíš najít uzel před posledním.

---

## Mazání podle hodnoty

První výskyt:

```python
lst.delete(10)
```

Všechny výskyty:

```python
count = lst.delete_all_occurrences(10)
```

---

## Přístup přes index

Linked list podporuje:

```python
print(lst[0])
print(lst[1])

lst[1] = 999
```

Ale pozor.

Tohle není Python `list`.

```python
lst[1000]
```

neznamená okamžitý přístup.

Musíš projít předchozí uzly:

```text
O(n)
```

---

## Iterace

Můžeš normálně:

```python
for value in lst:
    print(value)
```

V souboru je vlastní `LinkedListIterator`, který implementuje Python iterator protocol.

---

## PositionIterator

Repo obsahuje i druhý typ iterátoru, který se chová víc jako iterátory z C++ STL.

```python
it = lst.start_iter()

print(it.get_value())

it.move_to_next()

print(it.get_value())
```

K dispozici jsou například:

```python
start_iter()
end_iter()
find_iter()
get_value()
set_value()
move_to_next()
```

To se může hodit, pokud zadání nechce pracovat jen s indexy, ale přímo s **pozicemi v datové struktuře**.

---

## Sortování Linked Listu

Přímo `LinkedList` obsahuje:

```python
lst.selection_sort()
lst.insertion_sort()
lst.quick_sort()
```

Na rozdíl od funkcí v `sort.py` pracují tyto metody přímo s linked listem.

---

# 📚 Stack

Soubor:

```python
Stack.py
```

Stack funguje jako:

```text
LIFO
Last In, First Out
```

Představ si:

```text
    TOP
     ↓
   [30]
   [20]
   [10]
```

Když uděláš `pop()`, dostaneš `30`.

---

## Stack přes Linked List

```python
from Stack import Stack

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.top())
# 30

print(s.pop())
# 30
```

Základní operace:

```python
s.push(x)
s.pop()
s.top()
s.is_empty()
len(s)
```

Typicky:

```text
push: O(1)
pop:  O(1)
top:  O(1)
```

---

## Stack přes Python list

V souboru je také jednodušší varianta:

```python
from Stack import Stack1

s = Stack1()

s.push(10)
s.push(20)

print(s.pop())
```

`Stack1` interně používá normální Python:

```python
[]
```

Je dobrý, když potřebuješ pochopit samotný princip stacku bez řešení linked listu.

---

## Kdy stack vytáhnout?

Typické signály v zadání:

```text
LIFO
DFS
rekurze převedená na iteraci
kontrola závorek
undo
backtracking
vyhodnocování výrazů
```

Například kontrola závorek:

```text
( [ { } ] )
```

Otevírací závorky ukládáš na stack a při zavírací závorku kontroluješ vršek.

---

# 🚶 Queue

Ve `Stack.py` je také:

```python
Queue
```

Queue funguje:

```text
FIFO
First In, First Out
```

```text
vstup                         výstup
  ↓                              ↓
[30] <- [20] <- [10] <- [první]
```

Použití:

```python
from Stack import Queue

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.front())
# 10

print(q.dequeue())
# 10
```

Operace:

```python
q.enqueue(x)
q.dequeue()
q.front()
q.is_empty()
len(q)
```

Typicky:

```text
enqueue: O(1)
dequeue: O(1)
front:   O(1)
```

---

## Kdy queue?

Jakmile zadání říká nebo naznačuje:

```text
FIFO
BFS
průchod stromem po úrovních
zpracování ve stejném pořadí, v jakém data přišla
fronta úloh
```

tak pravděpodobně chceš queue.

---

# 🌳 Binary Search Tree

Soubor:

```python
BinarySearchTreePA.py
```

Import:

```python
from BinarySearchTreePA import BinarySearchTree
```

BST dodržuje:

```text
levý podstrom < uzel < pravý podstrom
```

Například:

```text
        8
       / \
      3   12
     / \    \
    1   6    20
```

---

# Vkládání

Iterativně:

```python
tree = BinarySearchTree()

tree.insert(8)
tree.insert(3)
tree.insert(12)
```

Rekurzivně:

```python
tree.insertR(8)
tree.insertR(3)
tree.insertR(12)
```

Duplicity se nevkládají.

---

# Hledání

Iterativní:

```python
node = tree.find(12)
```

Rekurzivní:

```python
node = tree.recursive_find(12)
```

Použití:

```python
if node is not None:
    print(node.data)
```

Složitost závisí na výšce stromu:

```text
O(h)
```

U rozumně vyváženého BST:

```text
O(log n)
```

U stromu:

```text
1
 \
  2
   \
    3
     \
      4
```

se z něj prakticky stane linked list:

```text
O(n)
```

---

# Minimum

V BST je nejmenší hodnota úplně vlevo.

```python
node = tree.find_min()

if node is not None:
    print(node.data)
```

Myšlenka:

```text
while node.left exists:
    node = node.left
```

---

# Počet uzlů

```python
print(tree.count())
```

Musíš navštívit celý strom:

```text
O(n)
```

---

# Hloubka stromu

```python
print(tree.depth())
```

Princip rekurzivně:

```text
depth(node) =
    1 + max(
        depth(left),
        depth(right)
    )
```

---

# Inorder traversal

```python
tree.print_inorder()
```

Pro BST má inorder velmi důležitou vlastnost:

```text
LEFT -> NODE -> RIGHT
```

vypíše hodnoty **vzestupně**.

Například:

```text
        8
       / \
      3   12
```

dostaneš:

```text
3 8 12
```

Tohle je jeden z nejčastějších triků u zkoušek.

---

# Preorder traversal

Základní pořadí:

```text
NODE -> LEFT -> RIGHT
```

Repo obsahuje například stackovou variantu:

```python
tree.print_preorder_stack()
```

Ta implementuje DFS bez rekurze pomocí zásobníku.

---

# Vypsání struktury stromu

```python
tree.print_structure()
```

Hodí se hlavně při debugování, protože podle odsazení vidíš hloubku jednotlivých uzlů.

---

# Kopie stromu

```python
new_tree = tree.copy()
```

Jedná se o hlubokou kopii.

Uzly nového stromu tedy nejsou stejné objekty jako uzly původního stromu.

---

# Vyvážený BST ze seřazeného pole

Pokud máš:

```python
a = [1, 2, 3, 4, 5, 6, 7]
```

můžeš vytvořit vyváženější strom:

```python
tree = BinarySearchTree.from_ordered_list_r(a)
```

Princip:

```text
vezmi prostředek jako kořen
        ↓
[1 2 3] 4 [5 6 7]
```

a rekurzivně udělej totéž vlevo a vpravo.

Výsledek přibližně:

```text
        4
      /   \
     2     6
    / \   / \
   1   3 5   7
```

Konstrukce je:

```text
O(n)
```

---

# ⚠️ Nedokončené části BST

Některé metody v `BinarySearchTreePA.py` jsou zatím jen připravené jako zadání a obsahují `...`.

Mezi ně patří například:

```python
delete()
serialize_to_list()
reconstruct_from_list()
print_by_levels_recursive()
print_by_levels_queue()
```

Takže před použitím:

```python
tree.delete(...)
```

se nejdřív podívej do zdrojáku.

Naopak například:

```python
find()
recursive_find()
insert()
insertR()
print_inorder()
count()
depth()
find_min()
copy()
print_preorder_stack()
from_ordered_list_r()
```

už implementaci mají.

---

# ⏱️ Tahák na složitosti

## Pole / sorty

| Algoritmus | Průměr | Nejhorší |
|---|---:|---:|
| Selection sort | O(n²) | O(n²) |
| Insertion sort | O(n²) | O(n²) |
| Bubble sort | O(n²) | O(n²) |
| Shaker sort | O(n²) | O(n²) |
| Quick sort | O(n log n) | O(n²) |

---

## Linked List

| Operace | Složitost |
|---|---:|
| vložení na začátek | O(1) |
| `append()` v této implementaci | O(1) |
| `first()` | O(1) |
| `remove_first()` | O(1) |
| hledání | O(n) |
| přístup přes index | O(n) |
| poslední prvek | O(n) |
| odstranění posledního | O(n) |

---

## Stack

| Operace | Složitost |
|---|---:|
| push | O(1) |
| pop | O(1) |
| top | O(1) |

---

## Queue

| Operace | Složitost |
|---|---:|
| enqueue | O(1) |
| dequeue | O(1) |
| front | O(1) |

---

## BST

Operace závisí na výšce stromu `h`.

| Operace | Vyvážený strom | Nejhorší případ |
|---|---:|---:|
| find | O(log n) | O(n) |
| insert | O(log n) | O(n) |
| minimum | O(log n) | O(n) |
| traversal | O(n) | O(n) |
| count | O(n) | O(n) |
| depth | O(n) | O(n) |

---

# 🧩 Rekurze vs. iterace

V repu je schválně několik věcí udělaných oběma způsoby.

Například hledání v BST:

```python
tree.find(x)
```

je iterativní.

```python
tree.recursive_find(x)
```

je rekurzivní.

U zkoušky se může objevit:

> „Implementujte algoritmus bez rekurze.“

Pak obvykle nahradíš call stack vlastním:

```text
Stack
```

Typický příklad:

```text
rekurzivní DFS
        ↓
iterativní DFS + Stack
```

A u BFS:

```text
Queue
```

---

# 🧠 Mini tahák před zkouškou

```text
STACK = LIFO
QUEUE = FIFO

DFS -> stack / rekurze
BFS -> queue

BST:
left < node < right

BST inorder:
left -> node -> right
= seřazené hodnoty

BST search:
O(h)

balanced BST:
h ≈ log n

Linked List:
rychlý začátek
pomalý index

Selection sort:
najdi minimum

Insertion sort:
vlož prvek do seřazené části

Bubble sort:
prohazuj sousedy

Quick sort:
pivot + partition + rekurze
```

---

# 🚨 Když něco nefunguje 5 minut před zkouškou

### `ModuleNotFoundError: _pytest`

```bash
python -m pip install pytest
```

nebo smaž nepotřebný import z `sort.py`.

---

### `ModuleNotFoundError: cgi`

Pravděpodobně používáš Python 3.13+.

Ze `Stack.py` odstraň:

```python
from cgi import test
```

Pro samotný stack není potřeba.

---

### Funkce vrací `None`

Podívej se, jestli uvnitř není jen:

```python
...
```

Část algoritmů je zatím připravená jako kostra k doplnění.

---

### Import má špatný název

Pozor na velikost písmen.

Aktuální názvy jsou:

```text
BinarySearchTreePA.py
LinkedList.py
Stack.py
sort.py
```

Tedy například:

```python
from BinarySearchTreePA import BinarySearchTree
from LinkedList import LinkedList
from Stack import Stack, Stack1, Queue
from sort import quick_sort
```

---

# 🎯 Jak se z toho učit

Nejlepší způsob není přečíst 500 řádků kódu.

Vyber si jednu věc a zkus:

1. nakreslit datovou strukturu na papír,
2. vysvětlit algoritmus vlastními slovy,
3. projít ručně malý vstup,
4. až potom se podívat do implementace,
5. implementaci zavřít a napsat ji znovu sám.

Například pro quicksort:

```text
[7, 2, 5, 1, 9]

1. vyber pivot
2. rozděl prvky
3. rekurzivně seřaď levou část
4. rekurzivně seřaď pravou část
```

Pokud zvládneš vysvětlit **proč každý krok existuje**, jsi na zkoušku mnohem lépe připravený než po naučení kódu nazpaměť.

---

# ✅ Co bych uměl před algoritmickou zkouškou

- [ ] napsat jednoduchý `LinkedList`
- [ ] vysvětlit sentinel node
- [ ] implementovat `push`, `pop`, `top`
- [ ] implementovat `enqueue`, `dequeue`
- [ ] poznat, kdy použít stack a kdy queue
- [ ] napsat insertion nebo selection sort
- [ ] vysvětlit quicksort a partition
- [ ] vysvětlit časovou složitost `O(n²)` vs. `O(n log n)`
- [ ] vložit prvek do BST
- [ ] najít prvek v BST
- [ ] vysvětlit preorder / inorder / postorder
- [ ] vědět, proč inorder BST vrací seřazené hodnoty
- [ ] vysvětlit DFS vs. BFS
- [ ] převést jednoduchou rekurzi na stack
- [ ] vysvětlit rozdíl mezi `O(log n)` a `O(n)` hledáním v BST

---

## GLHF 🍀

Repo ber jako tahák a referenci, ne jako kouzelnou hůlku.

Když algoritmus chápeš, pár řádků kódu si vždycky dostavíš. Když ho nechápeš, ani dokonale zkopírovaných 50 řádků tě před otázkou „a proč to funguje?“ nezachrání.
