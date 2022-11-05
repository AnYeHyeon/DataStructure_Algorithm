def is_validate_dom(dom_text : str) -> bool:
    """ dom 문서인 str 타입의 데이터를 받은 후 해당 데이터가 올바른 dom 문서인지 아닌지 확인 하는 코드 
        반드시 stack 또는 queue 를 사용하여 구현할 것
    Args:
        dom_text (str) : dom 문서

    Returns:
        is_valudate_dom (bool) : 해당 문서가 올바른 dom인지 확인하는 코드
    
    """
    dom_list = dom_text.split()
    text_list = ''

    for i in dom_list:
        text_list += i  
    element_node = dom_text.split("<")
    
    element_stack = []

    for node in element_node:
        element_stack.append(node)
        # print(element_stack)

        if '/' in node and '>' in node:  # 또 다른 방법으로는 정규표현식을 통해 </> 자체를 찾는 방법도 있음.
            to_index = node.find('>')  # 문자열의 index를 리턴
            tail_tag = node[1:to_index]  # '/' 빼고 tag명만 저장

            
            if tail_tag in element_stack[-2]:
                element_stack.pop()
                element_stack.pop()
                
                
    if element_stack == ['']:
        return True
    else:
        return False

if __name__ == "__main__":
    dom_text1 = """<data>
            <items>
                <item name="item1">item1abc</item>
                <item name="item2">item2abc</item>
            </items>
        </data>
        """.strip()

    dom_text2 = """<items>
             <data>
                 <items name="item1">item1abc</items>
                 <item name="item2">item2abc</item>
             </items>
         </data>
         """.strip()

    dom_text3 = """  <note>  
  <to>Tove</to>  
  <from>Jani</from>  
  <heading>Reminder</heading>  
  <body>Don't forget me this weekend!</body>  
</note>  
         """.strip()

    dom_text4 = """  <html lang="ko">
<head>
    
    <title>Document</title>
</head>
<body>
    
</body>
</html>  
         """.strip()    


    example = "<a>ddd</a>"

    result = is_validate_dom(dom_text4)
    print(result)