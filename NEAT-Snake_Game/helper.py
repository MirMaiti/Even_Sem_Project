import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot_scores_gen_wise(scores_gen):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Score')
    plt.xlabel('Generation')
    plt.ylabel('Score')
    plt.plot(scores_gen)
    # plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores_gen)-1, scores_gen[-1], str(scores_gen[-1]))
    # plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(10)
    plt.close()

def plot_abs_winner(scores,mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Winner_Stats')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(10)
    plt.close()
