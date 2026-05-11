# returns a new sorted array by the efficient variant of selection sort 
from _pytest.monkeypatch import K


def selection_sort(a):
    a = a[:]
    for i in range(len(a)):
        min_i = i
        min = a[i]
        for j in range(i+1, len(a)):
            if a[j] < min:
                min = a[j]
                min_i = j
        if min_i != i:
            a[min_i], a[i] = a[i], a[min_i]
    return a
    

# returns a new sorted array by the efficient variant of insertion sort 
def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        j = i
        akumulator = a[i]
        while (j > 0) and(a[j-1] > akumulator):  #prvek vlevo je větší
            j -= 1
        
        for k in range(1,i-j+1): #posunu prvky o jeden doprava
            a[i-k+1] = a[i-k]

        if i != j:
            a[j] = akumulator
    return a


# returns a new sorted array by the efficient variant of binary insertion sort 
def binary_insertion_sort(a):
   ...

# returns a new sorted array by shell sort 
def shell_sort(a):
    ...

# returns a new sorted array by the efficient variant of bubble sort 
def bubble_sort(a):
    a = a[:]
    prohozeni = True 
    k = len(a)-1 #index posledního prohození
    while prohozeni: #(seznam není seřazen)
        prohozeni = False #v daném průchodu došlo k aspoň jednomu prohození
        pom = k #poslední prohození při předchozím průchodu
        for i in range(pom):
            if a[i] > a[i+1]:
                prohozeni = True #seznam ještě není seřazen
                k = i
                a[i], a[i+1] = a[i+1], a[i]
    return a




# returns a new sorted array by shaker sort 
def shaker_sort(a):
    a = a[:]
    poslední_výměna = len(a) - 1 
    levy, pravy = 0, len(a) - 1

    while levy < pravy: #Cyklus přes konce intervalů
        for j in range(pravy, 0, -1): #Průchod od konce k počátku
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
                poslední_výměna = j #Index poslední výměny
        levy = poslední_výměna + 1 #příští cyklus až odsaď

        for j in range(levy, pravy + 1, 1): #Průchod od počátku ke konci
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
                poslední_výměna = j #Index poslední výměny
        pravy = poslední_výměna - 1 #příští cyklus jen posaď

    return a

# returns a new sorted array by merge sort 
def merge_sort(a):
   ...

# returns a new sorted array by heap sort 
def heap_sort(a):
   ...

# returns a new sorted array by quick sort 
def quick_sort(a):
   """recursive version of quick sort"""
   a = a[:]
   return _quick_sort(a, 0, len(a)-1)


def _quick_sort(a, levy, pravy):
    if levy >= pravy:
        return a
    pivot = _rozdel(a ,levy, pravy, ((levy + pravy) // 2))

    if pivot != levy:
        _quick_sort(a, levy, pivot - 1)
    if pivot != pravy:
        _quick_sort(a, pivot + 1, pravy)
    
    return a
    
    
            

def _rozdel(a, levy: int, pravy: int, i_pivot: int) -> int:
    """přijímá pole, indexy počátku a konce požadovaného úseku a index pivotu. Vrací index nového pivotu"""
    pivot = a[i_pivot]
    a[i_pivot], a[levy] = a[levy], a[i_pivot]
    i = levy + 1 
    k = pravy + 1 #poslední prvek menší jak pivot
    stejny = 0 #počet prvků rovných pivotu
    while i < k:
        if a[i] < pivot:
            i += 1 #nic nedělám, pokračuju dál
        else:
            k -= 1 
            a[i], a[k] = a[k], a[i]
    a[levy], a[k-1] = a[k-1], a[levy]
    return k-1



# returns the k-th smallest element in the array using hoare algorithm 
def hoare_algorithm(a, k):
   ...

# returns a new sorted array by radix sort 
def radix_sort(a, k=3):
   ...

# swaps a[i] and a[j] in a
def swap1(a, i, j):
    a[i], a[j] = a[j], a[i]
    return a

# swaps content of variables x and y 
def swap(x, y):
    return y, x

# simple test
def simple_test(sort_function, a):
    import random
    def single(a):
        r = sort_function(a)
        if r != sorted(a):
            print(f"{sort_function.__name__} error for: {a} with result: {r}")
            return False
        return True
    
    if not single(a):                       # original order
        return False
    if not single(sorted(a, reverse=True)): # descending order
        return False
    if not single(sorted(a)):               # ascending order
        return False
    for _ in range(10):
        shuffle_a = a[:]
        random.shuffle(shuffle_a)
        if not single(shuffle_a):           # random order
            return False
    return True

def sort_test():
    algorithms1 = [selection_sort, insertion_sort, binary_insertion_sort, bubble_sort, shaker_sort]
    algorithms2 = [merge_sort, heap_sort, quick_sort, radix_sort]
    algorithms3 = [selection_sort, insertion_sort, bubble_sort, shaker_sort, quick_sort] 
    a = [100, 2, 45, 13, 2, 90, 1, 3, 27]
    b = [100, 2, 45, 13, 2, 90, 1, 3, 27]
    c = [10]
    d = []
    for algorithm in algorithms3: # algorithms1 + algorithms2:
        test_ok = simple_test(algorithm, a)
        assert a == b, f"{algorithm.__name__}"
        if test_ok:
            test_ok = simple_test(algorithm, c)
        if test_ok:
            test_ok = simple_test(algorithm, d)
        if test_ok:
            print(f"Test on {algorithm.__name__} OK")

if __name__ == "__main__":
    sort_test()
    ...

