def count_item_and_sort(items):
    kamus = {}
    
    for i in items:
        if i in kamus:
            kamus[i] += 1
        else:
            kamus[i] = 1
    values = list(kamus.values())
    if len(set(values)) == len(values):
    # Jika semua nilai unik, maka urutkan berdasarkan nilai
        dict_sort = dict(sorted(kamus.items(), key=lambda item: item[1]))
    else:
    # Jika ada nilai yang sama, maka urutkan berdasarkan key
        dict_sort = dict(sorted(kamus.items(), key=lambda item: item[0]))        
        
    result = ' '.join([f"{key}->{value}" for key, value in dict_sort.items()])
    
    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"