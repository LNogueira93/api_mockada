class Demo():

    #  name, description, price, image, availibility, price_history, meta_tag, store_link

    def __init__(self, id_produto, name, description, price, image, availibility, price_history, meta_tag, store_link):
        self.id_produto = id_produto
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.availibility = availibility
        self.price_history = price_history
        self.meta_tag = meta_tag
        self.store_link = store_link

    def __dict__(self):
        d = dict()
        d["id_produto"] = self.id_produto
        d["name"] = self.name
        d["description"] = self.description
        d["price"] = self.price
        d["image"] = self.image
        d["availibility"] = self.availibility
        d["price_history"] = self.price_history
        d["meta_tag"] = self.meta_tag
        d["store_link"] = self.store_link
        return d

    def listar(dados):
        try:
            id_produto = dados["id_produto"]
            name = dados["name"]
            description = dados["description"]
            price = dados["price"]
            image = dados["image"]
            availibility = dados["availibility"]
            price_history = dados["price_history"]
            meta_tag = dados["meta_tag"]
            store_link = dados["store_link"]
            return Demo(id_produto=id_produto, name=name, description=description, price=price, image=image, availibility=availibility, price_history=price_history, meta_tag=meta_tag, store_link=store_link)
        except Exception as e:
            print("Problema ao listar seu produto!")
            print(e)

