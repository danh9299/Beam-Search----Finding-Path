#Đồ thị cây
graph = {
        'A': ['C','D','E'],
        'D': ['F','I'],
        'E': ['G','K'],
        'I': ['B','G'],
        'G': ['B','H'],
        'B':[],
        'C':[],
        'F':[],
        'H':[],
        'K':[]
        }
#Giá trị heuristic tại mỗi đỉnh
heuristic = {
        'A': 20,
        'C': 15,
        'D': 6,
        'E': 7,
        'F': 10,
        'I': 8,
        'G': 5,
        'K': 12,
        'B': 0,
        'H': 3,
            }
def beam_search(graph, start, end, k):
    #Tạo list open lưu trữ k đường đi tốt nhất
    open = []
    open.append(start)         
    while open:
        #Tạo 1 check để kiểm tra xem đã gặp end chưa
        check=0
        #Xóa Path để lưu lại k đường đi tốt nhất
        path=[]
        for i in range(0,len(open)):
            save = open.pop(0)
            path.append(save)
        #Lấy vị trí cuối cùng trong đường đi, tức bộ k nút tốt nhất mới được duyệt
        node = []
        save=''
        for i in range(0,len(path)):
            save = path[i][-1]
            node.append(save)
        print("Duyệt bộ nút tốt nhất: ",node)
        #Kiểm tra lại xem đã gặp điểm end chưa
        for i in range(0,len(path)):        
            if node[i] == end:
                check=check+1
        #Nếu đã thấy nghiệm rồi thì dừng thuật toán
        if(check!=0):
            return path
        #Tạo hàm child để lưu tất cả đường đi từ các nút đang xét tới các nút con của nó
        child=[]
        #Đẩy tất cả đường đi từ các nút đang xét tới các nút con của nó vào child
        for i in range(0,len(path)):
            for j in graph.get(node[i],[]):
                #Lấy ra đường đi đã có sẵn
                new_path=list(path[i])
                #Đẩy thêm nút con vào để extend đường đi
                new_path.append(j)
                #Cập nhật đường đi vào child
                child.append(new_path)
        #Sắp xếp lại child theo thứ tự tăng dần
        for i in range(0,len(child)-1):
            for j in range(i+1,len(child)):
                if(heuristic[child[i][-1]] > heuristic[child[j][-1]] ):          
                    a=child[i]
                    child[i]=child[j]
                    child[j]=a
        #Đẩy k đường đi đầu tiên trong child, tức k đường đi nhỏ nhất, vào trong open.
        #Trong trường hợp không đủ k thì đẩy toàn bộ đường đi trong child vào open
        if len(child)<k:                               
            for i in range(0,len(child)):
                open.append(child[i])
        else:
            for i in range(0,k):
                open.append(child[i])
    return path
#Phần main của bài
#Người dùng nhập vào dữ liệu cho điểm bắt đầu và điểm kết thúc
start = (input("Nhập điểm bắt đầu: "))
start = start.upper()
while start not in graph:
    print("Điểm bắt đầu phải có trong cây!")
    start = input("Nhập lại điểm bắt đầu: ")
    start = start.upper()
end = input("Nhập điểm cần đến: ")
end = end.upper()
while end not in graph:
    print("Điểm đến phải có trong cây!")
    end = input("Nhập lại điểm cần đến: ")
    end = end.upper()
k = input("Nhập k: ")
while k.isdigit()==False:
    print("Dữ liệu cho k phải là dạng số!")
    k = input("Nhập lại k: ")
k = int(k)
dem = 1
test_found = False
for x in beam_search(graph,start,end,k):
    if x[-1]==end:
        print("Đường đi thứ ",dem,": ",end="")
        dem = dem + 1
        test_found = True
    for y in x:
        if x[-1] == end:
            if y == start:
                print(y,end="")
            else:
                print("->",y,end="")
    print()
if test_found == False:
    print("Không tìm thấy đường đi")
        

