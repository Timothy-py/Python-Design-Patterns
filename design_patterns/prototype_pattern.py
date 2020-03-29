import copy


class Website:
    def __init__(self, name, domain, description, author, **kwargs):
        """Examples of optional attributes (kwargs):
            category, creation_date, technologies, keywords.
        """
        self.name = name
        self.domain = domain
        self.author = author
        self.description = description
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        summary = [f'Website "{self.name}"\n',]
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == 'name':
                continue
            summary.append(f"{attr}: {val}\n")
        return ''.join(summary)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj


def main():
    keywords = ('python', 'data', 'apis', 'automation')
    site1 = Website('ContentGardening', 'contentgardening.com', 'Automation and data-driven apps',
                    'Timothy', category='Blog', keywords=keywords)

    prototype = Prototype()
    identifier = 'ka-cg-1'
    prototype.register(identifier, site1)
    site2 = prototype.clone(identifier, name='My Blog',
                            domain="myblobspot.com",
                            description="A blog all about me",
                            category='Social',
                            creation_date='2020-03-29')

    # comparing the memory addresses of the two site objects

    for site in (site1, site2):
        print(site)
    print(f"ID site1 : {id(site1)} != ID site2 : {id(site2)}")


main()
