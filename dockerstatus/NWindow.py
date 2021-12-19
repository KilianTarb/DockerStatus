import curses

class NWindow():
    """
    On object init, initalises curses window and control keys.
    """

    def __init__(self) -> None:
        curses.wrapper(self.__main)
        self.DEFAULT_PAIR = 1
        self.COL_PAIR = 2
        self.SELECTED_PAIR = 3

        if curses.has_colors():
            curses.start_color()
            curses.init_pair(self.DEFAULT_PAIR, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(self.COL_PAIR, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(self.SELECTED_PAIR, curses.COLOR_BLACK, curses.COLOR_YELLOW)

        self.total_row_count = 0
        self.current_row = 0
        
    def __main(self, stdscr):
        self.stdscr = stdscr

    def create_table(self, cols) -> None:
        """
        cols {
            "name": str,
            "index": int
        }
        """
        self.col_start = []
        _, cols_max = self.stdscr.getmaxyx()
        divide_int = cols_max / len(cols)

        count = 0
        for i in cols:
            self.col_start.append(round(divide_int * count))
            self.stdscr.addstr(0, self.col_start[count], i['name'], curses.color_pair(self.COL_PAIR))
            count += 1
        self.total_row_count += 1

    def insert_row(self, row) -> None:
        """
        Insert a row with elements equal to the column count.
        """
        self.current_row += 1
        count = 0
        for i in row:
            if count >= len(row):
                continue
            self.stdscr.addstr(self.total_row_count, self.col_start[count], i, curses.color_pair(self.DEFAULT_PAIR))
            count += 1
        self.total_row_count += 1

    def wait_for_char(self):
        self.stdscr.getch()