import neat
from classes import *
from typing import List


def draw_window(win: pygame.Surface, birds: List[Bird], pipes: List[Pipe], base: Base, score: int, generation: int,
                highscore: int) -> None:
    win.blit(bg_img, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)

    for bird in birds:
        bird.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score), 1, WHITE_COLOR)
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    generation_label = STAT_FONT.render("Generation: " + str(generation - 1), 1, WHITE_COLOR)
    win.blit(generation_label, (10, 10))

    highscore_label = STAT_FONT.render("Highscore: " + str(highscore), 1, WHITE_COLOR)
    win.blit(highscore_label, (10, 70))

    pygame.display.update()


def eval_genomes(genomes: List[Tuple[int, neat.DefaultGenome]], config: neat.config.Config) -> None:
    global WIN, HIGHSCORE, gen
    win = WIN
    gen += 1

    nets = []
    birds = []
    ge = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(*BIRD_START_POSITION))
        ge.append(genome)

    base = Base(FLOOR)
    pipes = [Pipe(PIPE_POSITION)]
    score = 0

    clock = pygame.time.Clock()

    run = True
    while run and len(birds) > 0:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        pipe_index = 0

        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_index = 1

        for bird_id, bird in enumerate(birds):
            ge[bird_id].fitness += 0.1
            bird.move()

            output = nets[birds.index(bird)].activate(
                (bird.y, abs(bird.y - pipes[pipe_index].height), abs(bird.y - pipes[pipe_index].bottom)))

            if output[0] > 0.5:
                bird.jump()

        base.move()

        remove_pipes = []
        add_pipe = False

        for pipe in pipes:
            pipe.move()

            for bird_id, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[bird_id].fitness -= 1
                    birds.pop(bird_id)
                    nets.pop(bird_id)
                    ge.pop(bird_id)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)

        if add_pipe:
            score += 1

            if score > HIGHSCORE:
                HIGHSCORE = score

            for genome in ge:
                genome.fitness += 5
            pipes.append(Pipe(WIN_WIDTH))

        for pipe in remove_pipes:
            pipes.remove(pipe)

        for bird_id, bird in enumerate(birds):
            if bird.y + bird.img.get_height() - 10 >= FLOOR or bird.y < -50:
                birds.pop(bird_id)
                nets.pop(bird_id)
                ge.pop(bird_id)

        draw_window(win, birds, pipes, base, score, gen, HIGHSCORE)


def run(config_file: str) -> None:
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
