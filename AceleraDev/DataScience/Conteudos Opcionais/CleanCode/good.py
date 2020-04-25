from math import sqrt


class CalculaGeometria:
    @classmethod
    def volume_piramide(self, lado_base, altura):
        area_base = (lado_base ** 2 * sqrt(3)) / 4
        return (area_base * altura) * 3

def main():
    print(CalculaGeometria.volume_piramide(lado_base=3, altura=4))

if __name__ == '__main__':
    main()