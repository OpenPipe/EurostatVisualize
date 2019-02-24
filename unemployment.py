#
# Copyright 2019 João Pinto <lamego.pinto@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#%matplotlib qt

import seaborn as sns
import matplotlib.pyplot as plt

import pandas_datareader.data as web
data = web.DataReader("teilm020", 'eurostat')

# https://ec.europa.eu/eurostat/en/web/products-datasets/-/TEILM020
# Title, Age='Total', Sex in ['Total', 'Male', 'Female', SAD, Country, 'Montlhy']
country_data = data['Percentage of active population', 'Total', 'Total', 'Seasonally adjusted data, not calendar adjusted data']['Portugal']['Monthly']

ax = sns.barplot(x=country_data.index, y=country_data, color="skyblue")
ax.set_ylabel('Percentage from active population')
ax.set_xticklabels(country_data.index.strftime('%b %y'), rotation=30)

# Place as percentage
vals = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(x) for x in vals])

plt.title('Eurostat - Unemployment Rate - Portugal')

