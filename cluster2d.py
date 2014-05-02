from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# data generation

data_list = [-2.0690408488010572, -1.8286364124466166, -0.76533116255756983, -0.76533116255756983, -0.75302662983944124, -0.74771542406348046, -0.70731337976773023, -0.70196391793150015, -0.68955478110767121, -0.68162300918962315, -0.51853903094520026, -0.44667031342560054, -0.43325071106860985, -0.42923897669539091, -0.41135799952835672, -0.37762330347100237, -0.36492818112746095, -0.36148520906284198, -0.33648733709027595, -0.30576874026226419, -0.29316801778169482, -0.28325633903778019, -0.27428351456548639, -0.23698931370891785, -0.2344849776626024, -0.21105589327082719, -0.20235402038000744, -0.19375875646683127, -0.17853285360976087, -0.1726566180332387, -0.15953123105872088, -0.15675369749030468, -0.15306526228331385, -0.15152195626485224, -0.15077571402962714, -0.13931974640896164, -0.12797943189865654, -0.12659398058406665, -0.12522126882291715, -0.11785785854744915, -0.098896154702957553, -0.097109307117515253, -0.096968028545774396, -0.063844696364827036, -0.062653848750903809, -0.061417438446535286, -0.061373434082741672, -0.060656683031641984, -0.048794563866699094, -0.044705116254641783, -0.044007401325170135, -0.039652732459712355, -0.015765230835632402, -0.0016141555208578644, 0.0058497418742156403, 0.0070150588948386609, 0.010990300322298216, 0.018877985475004806, 0.025185417844137522, 0.026332461019525657, 0.035225821779600444, 0.036950916484214516, 0.041504986468763987, 0.045831864615629637, 0.060818775212300835, 0.065370851402194383, 0.071154916455198947, 0.072342275403856085, 0.079961830997019839, 0.083169073304792784, 0.083838274625589154, 0.087925118401647129, 0.088402312064601946, 0.088805207659541863, 0.090215964240387317, 0.097192065658435689, 0.10301170885436431, 0.10597044626609108, 0.10803715365007675, 0.10873903260623426, 0.12221244048014823, 0.1227528951171963, 0.13079486939411258, 0.13410214638467435, 0.14113185218237631, 0.14247000771723264, 0.14685279198075599, 0.14736580277625919, 0.16046350213705507, 0.1724971502519928, 0.17258227212485425, 0.17330705608556579, 0.17330705608556579, 0.17330705608556579, 0.17732345131400695, 0.18439851070156146, 0.18590314790662274, 0.1902244284507385, 0.19431631607838598, 0.1986798535597564, 0.19872040748958986, 0.2004414720122101, 0.20683593737516287, 0.21278434767458543, 0.21364547293682062, 0.21500827506442102, 0.21568575440072885, 0.21568575440072885, 0.21568575440072885, 0.21856483327579121, 0.21945027450910937, 0.21963127683571285, 0.22957190531678714, 0.23589084595084667, 0.2376490839729283, 0.23874075133678302, 0.23874075133678302, 0.23982946940978125, 0.24004931003469696, 0.24004931003469696, 0.24004931003469696, 0.24344891625615583, 0.24503633717939091, 0.24514887283079106, 0.24743313750435955, 0.24907905680877773, 0.253717101534218, 0.253717101534218, 0.25386400990942076, 0.25641725349684641, 0.25687143872336765, 0.25839228032503508, 0.26275104645412489, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26284795625313634, 0.26564635557567262, 0.27468812138344351, 0.27468812138344351, 0.27468812138344351, 0.27777617527645082, 0.27866854866604424, 0.27892380304009973, 0.28431665822655527, 0.30865648001212076, 0.30865648001212076, 0.34538067916918958, 0.3786081563017909, 0.38222469554455996, 0.3841167169927549, 0.68788832562086366]
d =  vstack(data_list)

data = vstack(rand(len(data_list),1) + array([.5,.5]))
print data


dat = np.insert(data, 1, data_list, axis=1)
print dat
#print dat
#data = vstack((t,c, d))
#print data
# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(dat,3)
# assign each sample to a cluster
idx,_ = vq(dat,centroids)

# some plotting using numpy's logical indexing
plot(dat[idx==0,0],dat[idx==0,1],'ob',
      dat[idx==1,0],dat[idx==1,1],'or',
      dat[idx==2,0],dat[idx==2,1],'ok',)
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(dat[idx==0,0],dat[idx==0,1], dat[idx==0,2], c='r', marker='o')
# ax.scatter(dat[idx==1,0],dat[idx==1,1], dat[idx==1,2], c='b', marker='o')
# ax.scatter(centroids[:,0],centroids[:,1], centroids[:,2], c='g', marker='s')
# plt.show()