def get_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },
    {
        'id': 2,
        'name': 'Tablet'
    }
    ]

def get_products(kw):
    products = [{
        'id':1,
        'name':'iPhone 13',
        'price':'20000000',
        'image': "https://synnexfpt.com/wp-content/uploads/2022/07/Apple-iPhone-13-mini-2.jpg"
    },
        {
            'id': 2,
            'name': 'iPhone 13 Pro',
            'price': '20000000',
            'image':"https://synnexfpt.com/wp-content/uploads/2022/06/iphone-13-pro-max-xanh-1.jpg"
        },
        {
            'id': 3,
            'name': 'iPhone 14',
            'price': '20000000',
            'image':"https://synnexfpt.com/wp-content/uploads/2022/06/Dien-thoai-di-dong-Apple-iPhone-15.jpg"
        },{
            'id': 4,
            'name': 'iPhone 14 Pro',
            'price': '20000000',
            'image':"https://product.hstatic.net/200000409445/product/14-max-tim_6dc05b654a3943fb8e9b03883b223d04_master.jpg"
        },{
            'id': 5,
            'name': 'iPhone 15',
            'price': '20000000',
            'image':"https://admin.hoanghamobile.com/Uploads/2023/09/14/vn-iphone-15-pink-pdp-image-position-1a-pink-color.jpg"
        },{
            'id': 6,
            'name': 'iPhone 15 Pro',
            'price':'20000000',
            'image': "https://nsv.by/upload/image_resize/6cc/3c6/51699f3bf56835cbadc68bb63c0ab9b4.webp"
        }
    ]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]

    return products