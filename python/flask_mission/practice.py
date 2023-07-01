total_pages = len(data) // per_page + (len(data) % per_page > 0)
start_index = per_page * (page - 1)
end_index = start_index + per_page
page_data = data[start_index:end_index]

# 받아와야하는 데이터 : 데이터, 페이지, 
def 