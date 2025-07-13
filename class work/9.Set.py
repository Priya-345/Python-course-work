#9.Set
#1.1.Creating a set
set = {1,2,3,4}
print(set) #{1, 2, 3, 4}

#1.2.Set with duplicate Elements
set1 = {1,2,3,4,2,5,3}
print(set1) #{1, 2, 3, 4, 5}

#2.Operations on Sets
#2.1.Membership Testiong
set3 = {1,2,3,4}
print(3 in set3) #True
print(5 not in set3) #True

#2.2.Union(| or union() method)
set4 = {1,2,3}
set5 = {4,5,6}
set6 = set4|set5 
print(set6) #{1, 2, 3, 4, 5, 6}

#2.3.Intersection(& or intersection() method)
set7 = {1,2,3}
set8 = {3,4,5}
set9 = set7 & set8
print(set9) #{3}

#2.4.Differencr(-or difference() method)
set10 = {1,2,3}
set11 = {3,4,5}
set12 = set10 - set11
print(set12) #{1, 2}

#2.5.Symmetric Difference(^ or symmetric_difference method)
set13 = {1,2,3}
set14 = {3,4,5}
set15 = set13 ^ set14
print(set15) #{1, 2, 4, 5}

#2.6.Subset(<=or isdubset() method)
set16 = {1,2,3,4}
set17 = {1,2,3,4,5}
print(set16 <= set17) #True

#2.7.Superset(>=or issuperset() method)
set18 = {1,2,3,4}
set19 = {1,2,3,4,5}
print(set18 >= set19) #False

#2.8.Disjoint set(isdisjoint() method)
set20 = {1,2,3}
set21 = {4,5,6,7}
print(set20.isdisjoint(set21)) #True

#3.Built-in Methods
#3.1.add()
set22 = {1,2,3,4,5}
set22.add(6)
print(set22) #{1, 2, 3, 4, 5, 6}

#3.2.remove()
set23 = {1,2,3,4,5,6}
set23.remove(6)
print(set23) #{1, 2, 3, 4, 5}

#3.3.Discard()
set24 = {1,2,3,4,5,6,7}
set24.discard(6)
print(set24) #{1, 2, 3, 4, 5, 7}

#3.4.pop()
set25 = {1,2,3,4,5}
set25.pop()
print(set25) #{2, 3, 4, 5}

#3.5.clear()
set26 = {1,2,3,4,5}
set26.clear()
print(set26) #set()

#3.6.Update
set27 = {1,2,3}
set27.update([3,4,5])
print(set27) #{1, 2, 3, 4, 5}

#3.7.Intersection_update()
set28 = {'apple','banana','cherry'}
set29 = {'google','microsoft','apple'}
set30 = {'apple','orange','kiwi'}
set28.intersection_update(set29,set30)
print(set28) #{'apple'}

#4.Built-in Function for set
set31 = {1,2,3,4,5}
print(len(set31)) #5
print(max(set31)) #5
print(min(set31)) #1
print(sorted(set31)) #[1, 2, 3, 4, 5]

#5.Frozenset
frozen = frozenset([1,2,3])
print(frozen) #frozenset({1, 2, 3})