from snake_square import SnakeSquare

# These constant assignments are redundant and
# already provide by Processing, however
# providing them here makes it possible to run
# tests in Pytest on functions using them.
UP, DOWN, LEFT, RIGHT = 38, 40, 37, 39


class Snake:
    """
    Snake class
    """

    def __init__(self, gc, player, controls):
        """
        Initialize snake
        GameController, String, Controls --> Snake
        """
        HUMAN_COLOR = (0.0, 0.0, 1.0)
        AI_COLOR = (1.0, 0.0, 0.0)
        MID_VERT = gc.h//2
        SNAKE_LENGTH = 5
        LEFT_START = SNAKE_LENGTH + 1
        RIGHT_START = gc.w - (SNAKE_LENGTH + 1)
        GROWTH_RATE = 3
        self.queue = []

        self._gc = gc
        if player == 'Human':
            self._player = 'Human'
            self._x = RIGHT_START
            self._y = MID_VERT
            self._set_dir('LEFT')
            self._dots_color = HUMAN_COLOR
        elif player == 'AI':
            self._player = 'AI'
            self._x = LEFT_START
            self._y = MID_VERT
            self._set_dir('RIGHT')
            self._dots_color = AI_COLOR

        self._len = SNAKE_LENGTH
        self._growth_rate = GROWTH_RATE
        self._body = [SnakeSquare(self._x-(self._x_dir)-(self._x_dir*b),
                                  self._y, self._dots_color)
                      for b in range(self._len)]
        self._gc.set_deadly_points([(b.x, b.y) for b in self._body])

        # Ensure that the player/AI snake controls have
        # access to this snake
        controls.set_snake(self)

    # Public methods
    def update(self, do_move):
        """
        Update snake's state
        Boolean --> None
        """
        # Determine whether to move
        self._update_move(do_move)
        self._display()

    def control(self, direction):
        """
        Control direction of the snake
        Direction --> None
        """
        # Prevent accidental reversals
        if direction == UP and self._dir != 'DOWN':
            self._set_dir('UP')
        elif direction == DOWN and self._dir != 'UP':
            self._set_dir('DOWN')
        elif direction == RIGHT and self._dir != 'LEFT':
            self._set_dir('RIGHT')
        elif direction == LEFT and self._dir != 'RIGHT':
            self._set_dir('LEFT')

    def grow(self):
        """
        Grow the snake by adding squares to
        the end of the snake
        None --> None
        """
        # TODO Problem 3: Implement snake growth.

        for i in range(len(self.queue)):
            temp_coordinate = self.queue.pop()
            self._body.append(SnakeSquare(
                temp_coordinate[0], temp_coordinate[1], self._dots_color))

        self._gc.set_deadly_points([(b.x, b.y) for b in self._body])

    def shrink(self):
        """
        Shrink the snake by removing squares from end
        None --> Boolean
        """
        loc = (self._body[0].x, self._body[0].y)
        self._gc.remove_deadly_point(
            (self._body[-1].x, self._body[-1].y)
        )
        self._body = self._body[:-1]
        # Let the caller know if we've hit zero length
        done = len(self._body) == 0
        return (done, loc if done else None)

    # Private methods
    def _update_move(self, do_move):

        # Move only if the do_move timer is true
        # and the body is longer than zero squares
        if (do_move and len(self._body)):
            self._gc.remove_deadly_point(
                (self._body[-1].x, self._body[-1].y)
            )
            # if the game starts, we need to record the coordinates one by one
            if len(self.queue) < self._growth_rate:
                self.queue.append((self._body[-1].x, self._body[-1].y))
            else:
                self.queue = self.queue[1:]
                # append the tail square to the queue
                self.queue.append((self._body[-1].x, self._body[-1].y))

            # Pass positions down from one square to the next
            for sq_i in range(len(self._body)-1, 0, -1):
                self._body[sq_i].x = self._body[sq_i-1].x
                self._body[sq_i].y = self._body[sq_i-1].y
            # Move the head
            self._move_head()

    def _move_head(self):
        """
        Move the snake's head
        None --> None
        """
        self._body[0].x += self._x_dir
        self._body[0].y += self._y_dir

        if self._body[0].x < 0:
            self._body[0].x = self._body[0].x+self._gc.w
        if self._body[0].x == self._gc.w:
            self._body[0].x = self._body[0].x-self._gc.w
        if self._body[0].y < 0:
            self._body[0].y = self._body[0].y+self._gc.h
        if self._body[0].y == self._gc.h:
            self._body[0].y = self._body[0].y-self._gc.h

        self._evaluate_head_placement()

    def _evaluate_head_placement(self):
        """
        Check for collision or apple eating for
        new head position
        None --> None
        """
        x, y = self._body[0].x, self._body[0].y
        if (x, y) in self._gc.deadly_points:
            self._gc.end_game(
                loser=self,
                event='Collision',
                location=(x, y)
            )
        else:
            self._gc.add_deadly_point((x, y))
            if (x == self._gc.apple.x and
                    y == self._gc.apple.y):
                self._gc.apple_eat(self)
                self._gc.set_apple()

    def _set_dir(self, dir):
        """
        Set the dir string attribute and x and y
        direction offset values
        String --> None
        """
        if dir == 'LEFT':
            self._dir = 'LEFT'
            self._x_dir = -1
            self._y_dir = 0
        elif dir == 'RIGHT':
            self._dir = 'RIGHT'
            self._x_dir = 1
            self._y_dir = 0
        elif dir == 'UP':
            self._dir = 'UP'
            self._x_dir = 0
            self._y_dir = -1
        elif dir == 'DOWN':
            self._dir = 'DOWN'
            self._x_dir = 0
            self._y_dir = 1

    def _display(self):
        """
        Display the snake
        None --> None
        """
        for sq in self._body:
            sq.display()

# Getters
    @property
    def body(self):
        """
        Getter for body
        None --> [SnakeSquare]
        """
        return self._body

    @property
    def player(self):
        """
        Getter for player value
        None --> String
        """
        return self._player
