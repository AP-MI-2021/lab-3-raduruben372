def print_menu():
    """
    afiseaza meniu
    :return:
    """
    print('''
1.Citire date.
2.Determinare cea mai lungă subsecvență cu proprietatea 1:Toate numerele sunt pare.
3.Determinare cea mai lungă subsecvență cu proprietatea 2:Toate numerele același număr de divizori.
4.Determinare cea mai lungă subsecvență cu proprietatea 3:Toate numerele sunt neprime.
5.Iesire
    ''')


def citire_lista():
    lst = []
    stringCitit = input("Dati lista(separata prin ,): ")
    numere = stringCitit.split(",")
    for x in numere:
        lst.append(int(x))
    return lst


def este_par(n):
    '''
    Verifica daca un numar este par
    :return:True daca numarul este par, False in caz contrar
    '''
    if n%2 == 0:
        return True
    return False


def test_este_par():
    assert este_par(2) is True
    assert  este_par(3) is False
    assert  este_par(1) is False


def toate_sunt_pare(lst):
    '''
    Verifica daca toate elementele din lista sunt pare
    :param lst: lista
    :return: True, daca toate elementele sunt pare, False in caz contrar
    '''
    for x in lst:
        if este_par(int(x)) is False:
            return False
    return True


def test_toate_sunt_pare():
    assert toate_sunt_pare([2,4,6,8]) is True
    assert toate_sunt_pare([1,3,6,3]) is False
    assert toate_sunt_pare([1,3]) is False


def get_longest_all_even(lst):
    '''
    Determina cea mai lunga secventa de nr. pare
    :param lst: lista nr
    :return: cea mai lunga secventa de nr. pare
    '''
    lst_max = []
    for i in range(0,len(lst)):
        for j in range(i,len(lst)):
            if toate_sunt_pare(lst[i:j+1]) and (len(lst[i:j+1]) > len(lst_max)):
                lst_max = lst[i:j+1]
    return lst_max


def test_get_longest_all_even():
    assert (get_longest_all_even([2,4,5]) == [2,4]) is True
    assert (get_longest_all_even([1,2,3,5,4]) == [2,4]) is False
    assert (get_longest_all_even([1,2,4,6]) == [2,4,6]) is True


def nr_divizori(n):
    '''
    determina numarul de divizori
    :param n: numar intreg
    :return: numarul de divizori
    '''
    p = 0
    if n == 1:
        return 1
    else:
        for i in range(1,n):
            if n % i == 0:
                p += 1
    return p


def test_nr_divizori():
    assert nr_divizori(3) == 1
    assert nr_divizori(5) == 1
    assert nr_divizori(10) == 3

def toate_au_acelasi_nr_de_divizori(lst):
    '''
    Verifica daca toate nr din lista au acelasi nr de divizori
    :param lst: lista cu numere
    :return: True daca toate nr din lista au acelasi nr de divizori, False in caz contrar
    '''
    p = nr_divizori(lst[0])
    for i in lst:
        if nr_divizori(i) != p:
            return False
    return True


def test_toate_au_acelasi_nr_de_divizori():
    assert toate_au_acelasi_nr_de_divizori([2,3,5]) is True
    assert toate_au_acelasi_nr_de_divizori([5,6,9,6,10]) is False
    assert toate_au_acelasi_nr_de_divizori([3,4,5]) is False


def get_longest_same_div_count(lst):
    '''
    determina cea mai lunga subsecventa de nr cu nr divizori egali
    :param lst:lista nr
    :return:cea mai lunga subsecventa de nr cu nr divizori egali
    '''
    lst_max = []
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if toate_au_acelasi_nr_de_divizori(lst[i:j+1]) and len(lst[i:j+1]) > len(lst_max):
                lst_max = lst[i:j+1]
    return lst_max


def test_get_longest_same_div_count():
    assert (get_longest_same_div_count([2,3,4]) == [2,3]) is True
    assert (get_longest_same_div_count([2,4,5,7]) == [5,7]) is True
    assert (get_longest_same_div_count([4,12]) == []) is True
    assert (get_longest_same_div_count([3,5,6]) == [3,5,6]) is False


def nu_este_prim(n):
    '''
    Determina daca un numar este neprim
    :param n: numar intreg
    :return: True daca n este neprim, False in caz contrar
    '''
    if n == 1:
        return True
    for i in range(2 , n):
         if n % i == 0:
              return True
    return False


def test_nu_este_prim():
    assert nu_este_prim(15) is True
    assert nu_este_prim(20) is True
    assert  nu_este_prim(1) is True
    assert  nu_este_prim(2) is False


def toate_sunt_neprime(lst):
    '''
    Verifica daca toate numerele din lista sunt neprime
    :param lst: lista numere
    :return: True daca toate numerele sunt neprime, False in caz contrar
    '''
    for i in lst:
        if nu_este_prim(i) is False:
            return False
    return True


def test_toate_sunt_neprime():
    assert toate_sunt_neprime([2,5,6,7,8]) is False
    assert toate_sunt_neprime([4,8,12]) is True
    assert toate_sunt_neprime([1,3,8,12]) is False


def get_longest_all_not_prime(lst):
    '''
    Determina cea mai lunga subsecventa cu numere neprime
    :param lst: lista cu numere
    :return: cea mai lunga subsecventa cu numere neprime
    '''
    lst_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toate_sunt_neprime(lst[i:j + 1]) is True and len(lst[i:j + 1]) > len(lst_max):
                lst_max = lst[i:j + 1]
    return lst_max


def test_get_longest_all_not_prime():
    assert (get_longest_all_not_prime([2,3,4,8,10]) == [4,8,10]) is True
    assert (get_longest_all_not_prime([2,1,3]) == [2,1]) is False
    assert (get_longest_all_not_prime([2,3,4,6,8,10]) == [4,6,8,10]) is True


def test():
    test_get_longest_all_even()
    test_toate_sunt_pare()
    test_este_par()
    test_nr_divizori()
    test_toate_au_acelasi_nr_de_divizori()
    test_nu_este_prim()
    test_toate_sunt_neprime()
    test_get_longest_all_not_prime()


def main():
    test()
    lst = []
    while True:
        print_menu()
        nr = int(input('Nr: '))
        if nr == 1:
            lst = citire_lista()
        elif nr == 2:
            if len(get_longest_all_even(lst)) == 0:
                print('Nu exista subsecventa')
            else:
                print('Cea mai lunga subsecventa: ',get_longest_all_even(lst))
        elif nr == 3:
            print('Cea mai lunga subsecventa: ',get_longest_same_div_count(lst))
        elif nr == 4:
            print('Cea mai lunga subsecventa: ',get_longest_all_not_prime(lst))
        elif nr == 5:
            break

if __name__ == '__main__':
    main()
