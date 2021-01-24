class Templates:
    def __init__(self):
        pass

    def gen_grid(self, width, height):
        arr = []
        for i in range(height):
            arr.append([0 for i in range(width)])
        return arr

    def create_methuselahs(self, type):
        # Make it so don't have to generate for each one
        self.map_array = self.gen_grid(100, 100)
        if type == 1:
            self.map_array[49][49] = 1
            self.map_array[48][48:50] = [1] * 2
            self.map_array[47][49:51] = [1] * 2
        elif type == 2:
            self.map_array[49][42] = 1
            print(len(self.map_array))
            self.map_array[49][46:49] = [1] * 3
            print(len(self.map_array[49]))
            self.map_array[48][41:43] = [1] * 2
            print(len(self.map_array))
            self.map_array[47][47] = 1
        elif type == 3:
            self.map_array[49][43:45] = [1] * 2
            self.map_array[49][47:50] = [1] * 3
            self.map_array[48][46] = 1
            self.map_array[47][44] = 1
        elif type == 4:
            # 47, x
            # 38, y
            self.map_array[50][47:50] = [1] * 3
            self.map_array[49][48] = 1
            self.map_array[48][48] = 1
            self.map_array[47][47:50] = [1] * 3
            self.map_array[45][47:50] = [1] * 3
            self.map_array[44][47:50] = [1] * 3
            self.map_array[42][47:50] = [1] * 3
            self.map_array[41][48] = 1
            self.map_array[40][48] = 1
            self.map_array[39][47:50] = [1] * 3
        return self.map_array

    def create_gosper_gun(self):
        # 14 - 50, x
        # 41 - 50, y
        self.map_array = self.gen_grid(100, 100)
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