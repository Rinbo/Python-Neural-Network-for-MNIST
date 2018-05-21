import mnist
import scipy.misc
import pandas as pd

#train_images = mnist.train_images()
##train_labels = mnist.train_labels()

test_images = mnist.test_images()
test_labels = mnist.test_labels()

#x = train_images.reshape((train_images.shape[0], train_images.shape[1] * train_images.shape[2]))
#y = train_labels.reshape((train_labels.shape[0], train_labels.shape[1] * train_labels.shape[2]))
xt = test_images.reshape((test_images.shape[0], test_images.shape[1] * test_images.shape[2]))
#yt = test_labels.reshape((test_labels.shape[0], test_labels.shape[1] * test_labels.shape[2]))

##pd.DataFrame(x).to_pickle('XTr.pickle')
##pd.DataFrame(train_labels).to_pickle('YTr.pickle')
##
pd.DataFrame(xt).to_pickle('XTe.pickle')
pd.DataFrame(test_labels).to_pickle('YTe.pickle')
