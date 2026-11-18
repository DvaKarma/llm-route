import unittest, json, route
R=json.load(open("regras.exemplo.json"))
class T(unittest.TestCase):
    def test(self):
        self.assertEqual(route.escolher(R,"corrigir bug no codigo",100),"modelo-codigo")
        self.assertEqual(route.escolher(R,"corrigir bug",90000),"modelo-medio")
        self.assertEqual(route.escolher(R,"faz um resumo"),"modelo-rapido")
unittest.main()
