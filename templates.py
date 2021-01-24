class Templates:
    def __init__(self, array):
        self.cur_array = array

    def gen_grid(self, width, height):
        arr = []
        for i in range(height):
            arr.append([0 for i in range(width)])
        return arr

    def create_methuselahs(self, type, pos):
        # Make it so don't have to generate for each one
        # Pos for = (x, y)
        self.map_array = self.cur_array
        if type == 1:
            self.map_array[pos[1]][pos[0]] = 1
            self.map_array[pos[1] - 1][pos[0] - 1:pos[0] + 1] = [1] * 2
            self.map_array[pos[1] - 2][pos[0]:pos[0] + 2] = [1] * 2
        elif type == 2:
            self.map_array[pos[1]][pos[0]] = 1
            self.map_array[pos[1]][pos[0] + 4:pos[0] + 7] = [1] * 3
            self.map_array[pos[1] - 1][pos[0] - 1:pos[0] + 1] = [1] * 2
            self.map_array[pos[1] - 2][pos[0] + 5] = 1
        elif type == 3:
            self.map_array[pos[1]][pos[0]:pos[0] + 2] = [1] * 2
            self.map_array[pos[1]][pos[0] + 4:pos[0] + 7] = [1] * 3
            self.map_array[pos[1] - 1][pos[0] + 3] = 1
            self.map_array[pos[1] - 2][pos[0] + 1] = 1
        return self.map_array

    def create_oscillator(self, type, pos):
        self.map_array = self.cur_array
        if type == 1:
            # 47, x
            # 38, y
            self.map_array[pos[1]][pos[0]:pos[0] + 3] = [1] * 3
            self.map_array[pos[1] - 1][pos[0] + 1] = 1
            self.map_array[pos[1] - 2][pos[0] + 1] = 1
            self.map_array[pos[1] - 3][pos[0]:pos[0] + 3] = [1] * 3
            self.map_array[pos[1] - 5][pos[0]:pos[0] + 3] = [1] * 3
            self.map_array[pos[1] - 6][pos[0]:pos[0] + 3] = [1] * 3
            self.map_array[pos[1] - 8][pos[0]:pos[0] + 3] = [1] * 3
            self.map_array[pos[1] - 9][pos[0] + 1] = 1
            self.map_array[pos[1] - 10][pos[0] + 1] = 1
            self.map_array[pos[1] - 11][pos[0]:pos[0] + 3] = [1] * 3

        return self.map_array

    def create_gosper_gun(self):
        # 14 - 50, x
        # 41 - 50, y
        self.map_array = self.gen_grid(100, 100)
        self.cur_array = self.map_array

        self.map_array[50][13:15] = [1] * 2
        self.map_array[49][12] = 1
        self.map_array[49][16] = 1
        self.map_array[48][11] = 1
        self.map_array[48][17] = 1
        self.map_array[48][25] = 1
        self.map_array[47][1:3] = [1] * 2
        self.map_array[47][11] = 1
        self.map_array[47][15] = 1
        self.map_array[47][17:19] = [1] * 2
        self.map_array[47][23] = 1
        self.map_array[47][25] = 1
        self.map_array[46][1:3] = [1] * 2
        self.map_array[46][17] = [1] * 2
        self.map_array[46][11] = 1
        self.map_array[46][17] = 1
        self.map_array[46][21:23] = [1] * 2
        self.map_array[45][12] = 1
        self.map_array[45][16] = 1
        self.map_array[45][21:23] = [1] * 2
        self.map_array[45][35:37] = [1] * 2
        self.map_array[44][13:15] = [1] * 2
        self.map_array[44][21:23] = [1] * 2
        self.map_array[44][35:37] = [1] * 2
        self.map_array[43][23] = 1
        self.map_array[43][25] = 1
        self.map_array[42][25] = 1



        return self.map_array