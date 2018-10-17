

```python
import pandas as pd
#input csv scrapy file as a dataframe
munging = pd.read_csv("scraping_file.csv")
```


```python
munging
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>&lt;h1&gt;Accidents &amp;amp; Disasters&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>3-Jan-16</td>
      <td>of $1k goal</td>
      <td>Elderly Couple's Home Burned</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>&lt;h1&gt;Accidents &amp;amp; Disasters&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>10-Jan-16</td>
      <td>of $3k goal</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>125</td>
      <td>&lt;h1&gt;Veterans &amp;amp; Heroes&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>29-Mar-14</td>
      <td>of £500 goal</td>
      <td>Raising funds for D-Day Landings Trip</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100</td>
      <td>&lt;h1&gt;Travel&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>1.0</td>
      <td>30-Oct-14</td>
      <td>of €175 goal</td>
      <td>By my VW</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>280</td>
      <td>&lt;h1&gt;Sports &amp;amp; Competitions&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>6.0</td>
      <td>7-Sep-16</td>
      <td>of €10k goal</td>
      <td>Help Despina to begin her way to Tokyo 2020</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2,500</td>
      <td>&lt;h1&gt;Political fundraising&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>36.0</td>
      <td>7-Sep-16</td>
      <td>of $2.5k goal</td>
      <td>Let's get Hilary elected in Ward 2!</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>&lt;h1&gt;Legal&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Mar-17</td>
      <td>of $5k goal</td>
      <td>Need a miracle of 5k, please help!</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>&lt;h1&gt;Health, Illness or Medical&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>3-Mar-18</td>
      <td>of $500 goal</td>
      <td>Help Marea get Enchroma glasses</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>&lt;h1&gt;Family &amp;amp; Kids&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>26-Oct-16</td>
      <td>of $25k goal</td>
      <td>Bring Kevin Home to his Family!</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>&lt;h1&gt;Faith, Missions &amp;amp; Religion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>22-Nov-15</td>
      <td>of $1.6k goal</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1,765</td>
      <td>&lt;h1&gt;Education &amp;amp; Schools&lt;/h1&gt;</td>
      <td>Singapore Dollar</td>
      <td>14.0</td>
      <td>11-May-17</td>
      <td>of $10k goal</td>
      <td>Sri Guru Granth Sahib Ji 3D</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5,110</td>
      <td>&lt;h1&gt;Education &amp;amp; Schools&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>10-Nov-17</td>
      <td>of $5k goal</td>
      <td>Art Day On-The-Go</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>400</td>
      <td>&lt;h1&gt;Business &amp;amp; Entrepreneurial&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>12.0</td>
      <td>20-Feb-16</td>
      <td>of €2k goal</td>
      <td>Gratis dating voor iedereen</td>
    </tr>
    <tr>
      <th>26</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>215</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>19.0</td>
      <td>9-May-17</td>
      <td>of £170 goal</td>
      <td>A Tablet for Ablazeko!</td>
    </tr>
    <tr>
      <th>28</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>20-Mar-12</td>
      <td>of $2k goal</td>
      <td>Mega Ran's Music Fund</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3740</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1,298</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>16-May-18</td>
      <td>of $3k goal</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
    </tr>
    <tr>
      <th>3742</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2,615</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>18-May-18</td>
      <td>of $3k goal</td>
      <td>Give us a chance</td>
    </tr>
    <tr>
      <th>3744</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>25-Jun-18</td>
      <td>of $10k goal</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
    </tr>
    <tr>
      <th>3746</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8,712</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>16-Aug-12</td>
      <td>of $10k goal</td>
      <td>Marshall County Animal Shelter</td>
    </tr>
    <tr>
      <th>3748</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>11-May-18</td>
      <td>of $5.5k goal</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
    </tr>
    <tr>
      <th>3750</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>522</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>11.0</td>
      <td>1-Jun-18</td>
      <td>of €680 goal</td>
      <td>URGENT!! Food needed for 65 dogs!!!!!!</td>
    </tr>
    <tr>
      <th>3752</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>4,724</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>102.0</td>
      <td>9-May-18</td>
      <td>of €4.5k goal</td>
      <td>**RAISED** April food for 500 dogs at The Bark...</td>
    </tr>
    <tr>
      <th>3754</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8,658</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>6-Jun-18</td>
      <td>of $7k goal</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
    </tr>
    <tr>
      <th>3756</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>3-Jul-18</td>
      <td>of $200 goal</td>
      <td>A016346 needs X-rays on his back leg.</td>
    </tr>
    <tr>
      <th>3758</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>187</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>28-Jun-18</td>
      <td>of €187 goal</td>
      <td>Please help me keep Ralph safe!!!</td>
    </tr>
    <tr>
      <th>3760</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>950</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>4.0</td>
      <td>10-Jul-18</td>
      <td>of $900 goal</td>
      <td>Help pay Habiba Shelter's rent and wages July</td>
    </tr>
    <tr>
      <th>3762</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>150</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>2.0</td>
      <td>18-Jun-18</td>
      <td>of €150 goal</td>
      <td>Badly injured tiny kitten needs special care/vet</td>
    </tr>
    <tr>
      <th>3764</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>160</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>26-May-18</td>
      <td>of £160 goal</td>
      <td>Help feed 70+ Egyptian rescue dogs for 1 month...</td>
    </tr>
    <tr>
      <th>3766</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>425</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>13.0</td>
      <td>3-May-18</td>
      <td>of €950 goal</td>
      <td>Mildred the Mastín deserves a new start to life.</td>
    </tr>
    <tr>
      <th>3768</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>23-Apr-18</td>
      <td>of $1.3k goal</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
    </tr>
  </tbody>
</table>
<p>3770 rows × 7 columns</p>
</div>




```python
#check to see how many null values there are.
munging.isna()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>9</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>10</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>11</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>12</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>13</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>15</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>16</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>17</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>18</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>19</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>20</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>21</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>22</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>23</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>24</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>25</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>26</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>27</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>28</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>29</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3740</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3742</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3744</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3746</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3748</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3750</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3752</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3754</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3756</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3758</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3760</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3762</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3764</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3766</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3768</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>3770 rows × 7 columns</p>
</div>




```python
#Drop any rows that have null values
munging = munging.dropna(axis = 0, how = 'any')
munging
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>&lt;h1&gt;Accidents &amp;amp; Disasters&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>3-Jan-16</td>
      <td>of $1k goal</td>
      <td>Elderly Couple's Home Burned</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>&lt;h1&gt;Accidents &amp;amp; Disasters&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>10-Jan-16</td>
      <td>of $3k goal</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
    </tr>
    <tr>
      <th>5</th>
      <td>125</td>
      <td>&lt;h1&gt;Veterans &amp;amp; Heroes&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>29-Mar-14</td>
      <td>of £500 goal</td>
      <td>Raising funds for D-Day Landings Trip</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100</td>
      <td>&lt;h1&gt;Travel&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>1.0</td>
      <td>30-Oct-14</td>
      <td>of €175 goal</td>
      <td>By my VW</td>
    </tr>
    <tr>
      <th>9</th>
      <td>280</td>
      <td>&lt;h1&gt;Sports &amp;amp; Competitions&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>6.0</td>
      <td>7-Sep-16</td>
      <td>of €10k goal</td>
      <td>Help Despina to begin her way to Tokyo 2020</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2,500</td>
      <td>&lt;h1&gt;Political fundraising&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>36.0</td>
      <td>7-Sep-16</td>
      <td>of $2.5k goal</td>
      <td>Let's get Hilary elected in Ward 2!</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>&lt;h1&gt;Legal&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Mar-17</td>
      <td>of $5k goal</td>
      <td>Need a miracle of 5k, please help!</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>&lt;h1&gt;Health, Illness or Medical&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>3-Mar-18</td>
      <td>of $500 goal</td>
      <td>Help Marea get Enchroma glasses</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>&lt;h1&gt;Family &amp;amp; Kids&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>26-Oct-16</td>
      <td>of $25k goal</td>
      <td>Bring Kevin Home to his Family!</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>&lt;h1&gt;Faith, Missions &amp;amp; Religion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>22-Nov-15</td>
      <td>of $1.6k goal</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1,765</td>
      <td>&lt;h1&gt;Education &amp;amp; Schools&lt;/h1&gt;</td>
      <td>Singapore Dollar</td>
      <td>14.0</td>
      <td>11-May-17</td>
      <td>of $10k goal</td>
      <td>Sri Guru Granth Sahib Ji 3D</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5,110</td>
      <td>&lt;h1&gt;Education &amp;amp; Schools&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>10-Nov-17</td>
      <td>of $5k goal</td>
      <td>Art Day On-The-Go</td>
    </tr>
    <tr>
      <th>25</th>
      <td>400</td>
      <td>&lt;h1&gt;Business &amp;amp; Entrepreneurial&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>12.0</td>
      <td>20-Feb-16</td>
      <td>of €2k goal</td>
      <td>Gratis dating voor iedereen</td>
    </tr>
    <tr>
      <th>27</th>
      <td>215</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>19.0</td>
      <td>9-May-17</td>
      <td>of £170 goal</td>
      <td>A Tablet for Ablazeko!</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>20-Mar-12</td>
      <td>of $2k goal</td>
      <td>Mega Ran's Music Fund</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1,605</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>32.0</td>
      <td>14-Jul-16</td>
      <td>of $1.8k goal</td>
      <td>Get Ya Boy Through His Last Year of School</td>
    </tr>
    <tr>
      <th>33</th>
      <td>970</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>24-Sep-14</td>
      <td>of $25k goal</td>
      <td>Christian Performing Arts Center Scholarship Fund</td>
    </tr>
    <tr>
      <th>35</th>
      <td>3,083</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>85.0</td>
      <td>4-Apr-15</td>
      <td>of $5k goal</td>
      <td>Please help us finish our film, "Mandarava".</td>
    </tr>
    <tr>
      <th>37</th>
      <td>100</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>23-May-17</td>
      <td>of $25k goal</td>
      <td>#lovebeatscancer - cancer fundriser May 30th 2017</td>
    </tr>
    <tr>
      <th>39</th>
      <td>450</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>7.0</td>
      <td>17-Mar-17</td>
      <td>of $4.2k goal</td>
      <td>Can/USA Early Music Tour with Benjamin Simao 2018</td>
    </tr>
    <tr>
      <th>41</th>
      <td>352</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>25-Mar-14</td>
      <td>of $1k goal</td>
      <td>Induct Cheap Trick Petition Campaign</td>
    </tr>
    <tr>
      <th>43</th>
      <td>4,910</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>33.0</td>
      <td>18-Apr-17</td>
      <td>of €4k goal</td>
      <td>Professional Aranea Highwind Project</td>
    </tr>
    <tr>
      <th>45</th>
      <td>830</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>15.0</td>
      <td>25-Apr-17</td>
      <td>of $5k goal</td>
      <td>Daughters Of Lilith</td>
    </tr>
    <tr>
      <th>47</th>
      <td>100</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>2.0</td>
      <td>16-Jun-17</td>
      <td>of $9k goal</td>
      <td>Help Serbinand say Hello..!</td>
    </tr>
    <tr>
      <th>49</th>
      <td>250</td>
      <td>&lt;h1&gt;Arts, Creative &amp;amp; Fashion&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2-Dec-16</td>
      <td>of $2.5k goal</td>
      <td>Statements Dance Company: Black Underground</td>
    </tr>
    <tr>
      <th>51</th>
      <td>697</td>
      <td>&lt;h1&gt;Business &amp;amp; Entrepreneurial&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>10.0</td>
      <td>10-Feb-16</td>
      <td>of €3.5k goal</td>
      <td>Aidez Ben à surpasser ses limites - Help Ben g...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>30,505</td>
      <td>&lt;h1&gt;Business &amp;amp; Entrepreneurial&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>27.0</td>
      <td>22-Feb-16</td>
      <td>of $30.4k goal</td>
      <td>Help CubbySpot Get a Government Grant</td>
    </tr>
    <tr>
      <th>55</th>
      <td>200</td>
      <td>&lt;h1&gt;Business &amp;amp; Entrepreneurial&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>1.0</td>
      <td>24-Mar-16</td>
      <td>of £200 goal</td>
      <td>I wanna crate campaign</td>
    </tr>
    <tr>
      <th>57</th>
      <td>430</td>
      <td>&lt;h1&gt;Business &amp;amp; Entrepreneurial&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>21-Mar-16</td>
      <td>of $400 goal</td>
      <td>Nothing's Simple A La Cart</td>
    </tr>
    <tr>
      <th>59</th>
      <td>505</td>
      <td>&lt;h1&gt;Business &amp;amp; Entrepreneurial&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>27-Nov-15</td>
      <td>of $2.5k goal</td>
      <td>Lawrence Hines NYC</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3711</th>
      <td>360</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>25-Feb-16</td>
      <td>of €4.5k goal</td>
      <td>Please help the refuge of Chios feed rescue dogs</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>140</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>22-Aug-18</td>
      <td>of $600 goal</td>
      <td>Paw-lease Help, Kaipo Needs Surgery!</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>725</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>25.0</td>
      <td>25-Aug-18</td>
      <td>of $1k goal</td>
      <td>Please help us pay for Remy's Parvo expenses.</td>
    </tr>
    <tr>
      <th>3717</th>
      <td>1,000</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>14.0</td>
      <td>25-Jul-18</td>
      <td>of £2.5k goal</td>
      <td>Reunite Roxie with her human</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>270</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>19-Aug-18</td>
      <td>of $680 goal</td>
      <td>Raising Money For Numbi's Oustanding Vet bills</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>430</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>11-Jul-18</td>
      <td>of $900 goal</td>
      <td>Zara &amp; Zack need help to find their forever homes</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>6,307</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>30-Oct-12</td>
      <td>of $2k goal</td>
      <td>Help us help those who can`t ask for help..</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>160</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>4.0</td>
      <td>20-Jul-18</td>
      <td>of €245 goal</td>
      <td>Please support Gray, Nera and Rocky in pension...</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>510</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Oct-13</td>
      <td>of $5k goal</td>
      <td>The Silver Lining Fund for Indigent Pets</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>800</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>22.0</td>
      <td>19-Jul-18</td>
      <td>of $1.5k goal</td>
      <td>Please help with Buck's medical bill</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>3,719</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>65.0</td>
      <td>3-Jul-18</td>
      <td>of $7k goal</td>
      <td>The Voiceless Dogs of Pawtcake refuge July 2018</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>225</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>27-Jul-18</td>
      <td>of $300 goal</td>
      <td>Help Hermione</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>240</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>9-Jul-18</td>
      <td>of $380 goal</td>
      <td>SURVIVOR, HERO NEEDS HELP TO GET TO HIS NEW HOME</td>
    </tr>
    <tr>
      <th>3737</th>
      <td>254</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>31-Jul-18</td>
      <td>of €200 goal</td>
      <td>Can We Help this Lady with her Cats and Kittens?</td>
    </tr>
    <tr>
      <th>3739</th>
      <td>938</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>23.0</td>
      <td>25-Jun-18</td>
      <td>of €1k goal</td>
      <td>Help for Furries June costs</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1,298</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>16-May-18</td>
      <td>of $3k goal</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2,615</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>18-May-18</td>
      <td>of $3k goal</td>
      <td>Give us a chance</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>25-Jun-18</td>
      <td>of $10k goal</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8,712</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>16-Aug-12</td>
      <td>of $10k goal</td>
      <td>Marshall County Animal Shelter</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>11-May-18</td>
      <td>of $5.5k goal</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>522</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>11.0</td>
      <td>1-Jun-18</td>
      <td>of €680 goal</td>
      <td>URGENT!! Food needed for 65 dogs!!!!!!</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>4,724</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>102.0</td>
      <td>9-May-18</td>
      <td>of €4.5k goal</td>
      <td>**RAISED** April food for 500 dogs at The Bark...</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8,658</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>6-Jun-18</td>
      <td>of $7k goal</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>3-Jul-18</td>
      <td>of $200 goal</td>
      <td>A016346 needs X-rays on his back leg.</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>187</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>28-Jun-18</td>
      <td>of €187 goal</td>
      <td>Please help me keep Ralph safe!!!</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>950</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Canadian Dollar</td>
      <td>4.0</td>
      <td>10-Jul-18</td>
      <td>of $900 goal</td>
      <td>Help pay Habiba Shelter's rent and wages July</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>150</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>2.0</td>
      <td>18-Jun-18</td>
      <td>of €150 goal</td>
      <td>Badly injured tiny kitten needs special care/vet</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>160</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>26-May-18</td>
      <td>of £160 goal</td>
      <td>Help feed 70+ Egyptian rescue dogs for 1 month...</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>425</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>Euro</td>
      <td>13.0</td>
      <td>3-May-18</td>
      <td>of €950 goal</td>
      <td>Mildred the Mastín deserves a new start to life.</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>&lt;h1&gt;Animals, Pets &amp;amp; Humane&lt;/h1&gt;</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>23-Apr-18</td>
      <td>of $1.3k goal</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
    </tr>
  </tbody>
</table>
<p>1885 rows × 7 columns</p>
</div>




```python
#use string replace and regex to strip html tags and various other useless info
munging['category'] = munging.category.str.replace('^<...', '').str.replace('amp;', '').str.replace('</h1>', '')
munging
```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>3-Jan-16</td>
      <td>of $1k goal</td>
      <td>Elderly Couple's Home Burned</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>10-Jan-16</td>
      <td>of $3k goal</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
    </tr>
    <tr>
      <th>5</th>
      <td>125</td>
      <td>Veterans &amp; Heroes</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>29-Mar-14</td>
      <td>of £500 goal</td>
      <td>Raising funds for D-Day Landings Trip</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100</td>
      <td>Travel</td>
      <td>Euro</td>
      <td>1.0</td>
      <td>30-Oct-14</td>
      <td>of €175 goal</td>
      <td>By my VW</td>
    </tr>
    <tr>
      <th>9</th>
      <td>280</td>
      <td>Sports &amp; Competitions</td>
      <td>Euro</td>
      <td>6.0</td>
      <td>7-Sep-16</td>
      <td>of €10k goal</td>
      <td>Help Despina to begin her way to Tokyo 2020</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2,500</td>
      <td>Political fundraising</td>
      <td>Canadian Dollar</td>
      <td>36.0</td>
      <td>7-Sep-16</td>
      <td>of $2.5k goal</td>
      <td>Let's get Hilary elected in Ward 2!</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>Legal</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Mar-17</td>
      <td>of $5k goal</td>
      <td>Need a miracle of 5k, please help!</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>Health, Illness or Medical</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>3-Mar-18</td>
      <td>of $500 goal</td>
      <td>Help Marea get Enchroma glasses</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>Family &amp; Kids</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>26-Oct-16</td>
      <td>of $25k goal</td>
      <td>Bring Kevin Home to his Family!</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>Faith, Missions &amp; Religion</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>22-Nov-15</td>
      <td>of $1.6k goal</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1,765</td>
      <td>Education &amp; Schools</td>
      <td>Singapore Dollar</td>
      <td>14.0</td>
      <td>11-May-17</td>
      <td>of $10k goal</td>
      <td>Sri Guru Granth Sahib Ji 3D</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5,110</td>
      <td>Education &amp; Schools</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>10-Nov-17</td>
      <td>of $5k goal</td>
      <td>Art Day On-The-Go</td>
    </tr>
    <tr>
      <th>25</th>
      <td>400</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>12.0</td>
      <td>20-Feb-16</td>
      <td>of €2k goal</td>
      <td>Gratis dating voor iedereen</td>
    </tr>
    <tr>
      <th>27</th>
      <td>215</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Pound Sterling</td>
      <td>19.0</td>
      <td>9-May-17</td>
      <td>of £170 goal</td>
      <td>A Tablet for Ablazeko!</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>20-Mar-12</td>
      <td>of $2k goal</td>
      <td>Mega Ran's Music Fund</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1,605</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>32.0</td>
      <td>14-Jul-16</td>
      <td>of $1.8k goal</td>
      <td>Get Ya Boy Through His Last Year of School</td>
    </tr>
    <tr>
      <th>33</th>
      <td>970</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>24-Sep-14</td>
      <td>of $25k goal</td>
      <td>Christian Performing Arts Center Scholarship Fund</td>
    </tr>
    <tr>
      <th>35</th>
      <td>3,083</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>85.0</td>
      <td>4-Apr-15</td>
      <td>of $5k goal</td>
      <td>Please help us finish our film, "Mandarava".</td>
    </tr>
    <tr>
      <th>37</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>23-May-17</td>
      <td>of $25k goal</td>
      <td>#lovebeatscancer - cancer fundriser May 30th 2017</td>
    </tr>
    <tr>
      <th>39</th>
      <td>450</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>7.0</td>
      <td>17-Mar-17</td>
      <td>of $4.2k goal</td>
      <td>Can/USA Early Music Tour with Benjamin Simao 2018</td>
    </tr>
    <tr>
      <th>41</th>
      <td>352</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>25-Mar-14</td>
      <td>of $1k goal</td>
      <td>Induct Cheap Trick Petition Campaign</td>
    </tr>
    <tr>
      <th>43</th>
      <td>4,910</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Euro</td>
      <td>33.0</td>
      <td>18-Apr-17</td>
      <td>of €4k goal</td>
      <td>Professional Aranea Highwind Project</td>
    </tr>
    <tr>
      <th>45</th>
      <td>830</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>15.0</td>
      <td>25-Apr-17</td>
      <td>of $5k goal</td>
      <td>Daughters Of Lilith</td>
    </tr>
    <tr>
      <th>47</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>2.0</td>
      <td>16-Jun-17</td>
      <td>of $9k goal</td>
      <td>Help Serbinand say Hello..!</td>
    </tr>
    <tr>
      <th>49</th>
      <td>250</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2-Dec-16</td>
      <td>of $2.5k goal</td>
      <td>Statements Dance Company: Black Underground</td>
    </tr>
    <tr>
      <th>51</th>
      <td>697</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>10.0</td>
      <td>10-Feb-16</td>
      <td>of €3.5k goal</td>
      <td>Aidez Ben à surpasser ses limites - Help Ben g...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>30,505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Canadian Dollar</td>
      <td>27.0</td>
      <td>22-Feb-16</td>
      <td>of $30.4k goal</td>
      <td>Help CubbySpot Get a Government Grant</td>
    </tr>
    <tr>
      <th>55</th>
      <td>200</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Pound Sterling</td>
      <td>1.0</td>
      <td>24-Mar-16</td>
      <td>of £200 goal</td>
      <td>I wanna crate campaign</td>
    </tr>
    <tr>
      <th>57</th>
      <td>430</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>21-Mar-16</td>
      <td>of $400 goal</td>
      <td>Nothing's Simple A La Cart</td>
    </tr>
    <tr>
      <th>59</th>
      <td>505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>27-Nov-15</td>
      <td>of $2.5k goal</td>
      <td>Lawrence Hines NYC</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3711</th>
      <td>360</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>25-Feb-16</td>
      <td>of €4.5k goal</td>
      <td>Please help the refuge of Chios feed rescue dogs</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>140</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>22-Aug-18</td>
      <td>of $600 goal</td>
      <td>Paw-lease Help, Kaipo Needs Surgery!</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>725</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>25.0</td>
      <td>25-Aug-18</td>
      <td>of $1k goal</td>
      <td>Please help us pay for Remy's Parvo expenses.</td>
    </tr>
    <tr>
      <th>3717</th>
      <td>1,000</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>14.0</td>
      <td>25-Jul-18</td>
      <td>of £2.5k goal</td>
      <td>Reunite Roxie with her human</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>270</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>19-Aug-18</td>
      <td>of $680 goal</td>
      <td>Raising Money For Numbi's Oustanding Vet bills</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>430</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>11-Jul-18</td>
      <td>of $900 goal</td>
      <td>Zara &amp; Zack need help to find their forever homes</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>6,307</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>30-Oct-12</td>
      <td>of $2k goal</td>
      <td>Help us help those who can`t ask for help..</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>4.0</td>
      <td>20-Jul-18</td>
      <td>of €245 goal</td>
      <td>Please support Gray, Nera and Rocky in pension...</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>510</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Oct-13</td>
      <td>of $5k goal</td>
      <td>The Silver Lining Fund for Indigent Pets</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>800</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>22.0</td>
      <td>19-Jul-18</td>
      <td>of $1.5k goal</td>
      <td>Please help with Buck's medical bill</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>3,719</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>65.0</td>
      <td>3-Jul-18</td>
      <td>of $7k goal</td>
      <td>The Voiceless Dogs of Pawtcake refuge July 2018</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>225</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>27-Jul-18</td>
      <td>of $300 goal</td>
      <td>Help Hermione</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>9-Jul-18</td>
      <td>of $380 goal</td>
      <td>SURVIVOR, HERO NEEDS HELP TO GET TO HIS NEW HOME</td>
    </tr>
    <tr>
      <th>3737</th>
      <td>254</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>31-Jul-18</td>
      <td>of €200 goal</td>
      <td>Can We Help this Lady with her Cats and Kittens?</td>
    </tr>
    <tr>
      <th>3739</th>
      <td>938</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>23.0</td>
      <td>25-Jun-18</td>
      <td>of €1k goal</td>
      <td>Help for Furries June costs</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1,298</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>16-May-18</td>
      <td>of $3k goal</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2,615</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>18-May-18</td>
      <td>of $3k goal</td>
      <td>Give us a chance</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>25-Jun-18</td>
      <td>of $10k goal</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8,712</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>16-Aug-12</td>
      <td>of $10k goal</td>
      <td>Marshall County Animal Shelter</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>11-May-18</td>
      <td>of $5.5k goal</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>522</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>11.0</td>
      <td>1-Jun-18</td>
      <td>of €680 goal</td>
      <td>URGENT!! Food needed for 65 dogs!!!!!!</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>4,724</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>102.0</td>
      <td>9-May-18</td>
      <td>of €4.5k goal</td>
      <td>**RAISED** April food for 500 dogs at The Bark...</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8,658</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>6-Jun-18</td>
      <td>of $7k goal</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>3-Jul-18</td>
      <td>of $200 goal</td>
      <td>A016346 needs X-rays on his back leg.</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>187</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>28-Jun-18</td>
      <td>of €187 goal</td>
      <td>Please help me keep Ralph safe!!!</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Canadian Dollar</td>
      <td>4.0</td>
      <td>10-Jul-18</td>
      <td>of $900 goal</td>
      <td>Help pay Habiba Shelter's rent and wages July</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>150</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>2.0</td>
      <td>18-Jun-18</td>
      <td>of €150 goal</td>
      <td>Badly injured tiny kitten needs special care/vet</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>26-May-18</td>
      <td>of £160 goal</td>
      <td>Help feed 70+ Egyptian rescue dogs for 1 month...</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>425</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>13.0</td>
      <td>3-May-18</td>
      <td>of €950 goal</td>
      <td>Mildred the Mastín deserves a new start to life.</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>23-Apr-18</td>
      <td>of $1.3k goal</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
    </tr>
  </tbody>
</table>
<p>1885 rows × 7 columns</p>
</div>








```python
#get rid of string characters to easily convert values to numeric.
munging['target'] = munging.target.str.replace('of|goal' , '')
munging
```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>3-Jan-16</td>
      <td>$1k</td>
      <td>Elderly Couple's Home Burned</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>10-Jan-16</td>
      <td>$3k</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
    </tr>
    <tr>
      <th>5</th>
      <td>125</td>
      <td>Veterans &amp; Heroes</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>29-Mar-14</td>
      <td>£500</td>
      <td>Raising funds for D-Day Landings Trip</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100</td>
      <td>Travel</td>
      <td>Euro</td>
      <td>1.0</td>
      <td>30-Oct-14</td>
      <td>€175</td>
      <td>By my VW</td>
    </tr>
    <tr>
      <th>9</th>
      <td>280</td>
      <td>Sports &amp; Competitions</td>
      <td>Euro</td>
      <td>6.0</td>
      <td>7-Sep-16</td>
      <td>€10k</td>
      <td>Help Despina to begin her way to Tokyo 2020</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2,500</td>
      <td>Political fundraising</td>
      <td>Canadian Dollar</td>
      <td>36.0</td>
      <td>7-Sep-16</td>
      <td>$2.5k</td>
      <td>Let's get Hilary elected in Ward 2!</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>Legal</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Mar-17</td>
      <td>$5k</td>
      <td>Need a miracle of 5k, please help!</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>Health, Illness or Medical</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>3-Mar-18</td>
      <td>$500</td>
      <td>Help Marea get Enchroma glasses</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>Family &amp; Kids</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>26-Oct-16</td>
      <td>$25k</td>
      <td>Bring Kevin Home to his Family!</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>Faith, Missions &amp; Religion</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>22-Nov-15</td>
      <td>$1.6k</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1,765</td>
      <td>Education &amp; Schools</td>
      <td>Singapore Dollar</td>
      <td>14.0</td>
      <td>11-May-17</td>
      <td>$10k</td>
      <td>Sri Guru Granth Sahib Ji 3D</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5,110</td>
      <td>Education &amp; Schools</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>10-Nov-17</td>
      <td>$5k</td>
      <td>Art Day On-The-Go</td>
    </tr>
    <tr>
      <th>25</th>
      <td>400</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>12.0</td>
      <td>20-Feb-16</td>
      <td>€2k</td>
      <td>Gratis dating voor iedereen</td>
    </tr>
    <tr>
      <th>27</th>
      <td>215</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Pound Sterling</td>
      <td>19.0</td>
      <td>9-May-17</td>
      <td>£170</td>
      <td>A Tablet for Ablazeko!</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>20-Mar-12</td>
      <td>$2k</td>
      <td>Mega Ran's Music Fund</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1,605</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>32.0</td>
      <td>14-Jul-16</td>
      <td>$1.8k</td>
      <td>Get Ya Boy Through His Last Year of School</td>
    </tr>
    <tr>
      <th>33</th>
      <td>970</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>24-Sep-14</td>
      <td>$25k</td>
      <td>Christian Performing Arts Center Scholarship Fund</td>
    </tr>
    <tr>
      <th>35</th>
      <td>3,083</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>85.0</td>
      <td>4-Apr-15</td>
      <td>$5k</td>
      <td>Please help us finish our film, "Mandarava".</td>
    </tr>
    <tr>
      <th>37</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>23-May-17</td>
      <td>$25k</td>
      <td>#lovebeatscancer - cancer fundriser May 30th 2017</td>
    </tr>
    <tr>
      <th>39</th>
      <td>450</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>7.0</td>
      <td>17-Mar-17</td>
      <td>$4.2k</td>
      <td>Can/USA Early Music Tour with Benjamin Simao 2018</td>
    </tr>
    <tr>
      <th>41</th>
      <td>352</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>25-Mar-14</td>
      <td>$1k</td>
      <td>Induct Cheap Trick Petition Campaign</td>
    </tr>
    <tr>
      <th>43</th>
      <td>4,910</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Euro</td>
      <td>33.0</td>
      <td>18-Apr-17</td>
      <td>€4k</td>
      <td>Professional Aranea Highwind Project</td>
    </tr>
    <tr>
      <th>45</th>
      <td>830</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>15.0</td>
      <td>25-Apr-17</td>
      <td>$5k</td>
      <td>Daughters Of Lilith</td>
    </tr>
    <tr>
      <th>47</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>2.0</td>
      <td>16-Jun-17</td>
      <td>$9k</td>
      <td>Help Serbinand say Hello..!</td>
    </tr>
    <tr>
      <th>49</th>
      <td>250</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2-Dec-16</td>
      <td>$2.5k</td>
      <td>Statements Dance Company: Black Underground</td>
    </tr>
    <tr>
      <th>51</th>
      <td>697</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>10.0</td>
      <td>10-Feb-16</td>
      <td>€3.5k</td>
      <td>Aidez Ben à surpasser ses limites - Help Ben g...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>30,505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Canadian Dollar</td>
      <td>27.0</td>
      <td>22-Feb-16</td>
      <td>$30.4k</td>
      <td>Help CubbySpot Get a Government Grant</td>
    </tr>
    <tr>
      <th>55</th>
      <td>200</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Pound Sterling</td>
      <td>1.0</td>
      <td>24-Mar-16</td>
      <td>£200</td>
      <td>I wanna crate campaign</td>
    </tr>
    <tr>
      <th>57</th>
      <td>430</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>21-Mar-16</td>
      <td>$400</td>
      <td>Nothing's Simple A La Cart</td>
    </tr>
    <tr>
      <th>59</th>
      <td>505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>27-Nov-15</td>
      <td>$2.5k</td>
      <td>Lawrence Hines NYC</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3711</th>
      <td>360</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>25-Feb-16</td>
      <td>€4.5k</td>
      <td>Please help the refuge of Chios feed rescue dogs</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>140</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>22-Aug-18</td>
      <td>$600</td>
      <td>Paw-lease Help, Kaipo Needs Surgery!</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>725</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>25.0</td>
      <td>25-Aug-18</td>
      <td>$1k</td>
      <td>Please help us pay for Remy's Parvo expenses.</td>
    </tr>
    <tr>
      <th>3717</th>
      <td>1,000</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>14.0</td>
      <td>25-Jul-18</td>
      <td>£2.5k</td>
      <td>Reunite Roxie with her human</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>270</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>19-Aug-18</td>
      <td>$680</td>
      <td>Raising Money For Numbi's Oustanding Vet bills</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>430</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>11-Jul-18</td>
      <td>$900</td>
      <td>Zara &amp; Zack need help to find their forever homes</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>6,307</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>30-Oct-12</td>
      <td>$2k</td>
      <td>Help us help those who can`t ask for help..</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>4.0</td>
      <td>20-Jul-18</td>
      <td>€245</td>
      <td>Please support Gray, Nera and Rocky in pension...</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>510</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Oct-13</td>
      <td>$5k</td>
      <td>The Silver Lining Fund for Indigent Pets</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>800</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>22.0</td>
      <td>19-Jul-18</td>
      <td>$1.5k</td>
      <td>Please help with Buck's medical bill</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>3,719</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>65.0</td>
      <td>3-Jul-18</td>
      <td>$7k</td>
      <td>The Voiceless Dogs of Pawtcake refuge July 2018</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>225</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>27-Jul-18</td>
      <td>$300</td>
      <td>Help Hermione</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>9-Jul-18</td>
      <td>$380</td>
      <td>SURVIVOR, HERO NEEDS HELP TO GET TO HIS NEW HOME</td>
    </tr>
    <tr>
      <th>3737</th>
      <td>254</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>31-Jul-18</td>
      <td>€200</td>
      <td>Can We Help this Lady with her Cats and Kittens?</td>
    </tr>
    <tr>
      <th>3739</th>
      <td>938</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>23.0</td>
      <td>25-Jun-18</td>
      <td>€1k</td>
      <td>Help for Furries June costs</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1,298</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>16-May-18</td>
      <td>$3k</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2,615</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>18-May-18</td>
      <td>$3k</td>
      <td>Give us a chance</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>25-Jun-18</td>
      <td>$10k</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8,712</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>16-Aug-12</td>
      <td>$10k</td>
      <td>Marshall County Animal Shelter</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>11-May-18</td>
      <td>$5.5k</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>522</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>11.0</td>
      <td>1-Jun-18</td>
      <td>€680</td>
      <td>URGENT!! Food needed for 65 dogs!!!!!!</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>4,724</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>102.0</td>
      <td>9-May-18</td>
      <td>€4.5k</td>
      <td>**RAISED** April food for 500 dogs at The Bark...</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8,658</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>6-Jun-18</td>
      <td>$7k</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>3-Jul-18</td>
      <td>$200</td>
      <td>A016346 needs X-rays on his back leg.</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>187</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>28-Jun-18</td>
      <td>€187</td>
      <td>Please help me keep Ralph safe!!!</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Canadian Dollar</td>
      <td>4.0</td>
      <td>10-Jul-18</td>
      <td>$900</td>
      <td>Help pay Habiba Shelter's rent and wages July</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>150</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>2.0</td>
      <td>18-Jun-18</td>
      <td>€150</td>
      <td>Badly injured tiny kitten needs special care/vet</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>26-May-18</td>
      <td>£160</td>
      <td>Help feed 70+ Egyptian rescue dogs for 1 month...</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>425</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>13.0</td>
      <td>3-May-18</td>
      <td>€950</td>
      <td>Mildred the Mastín deserves a new start to life.</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>23-Apr-18</td>
      <td>$1.3k</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
    </tr>
  </tbody>
</table>
<p>1885 rows × 7 columns</p>
</div>




```python
#get rid of currncey symbols

munging['target'] = munging.target.str.replace('\$|£|€|₽|kr|₱|Fr|₪|฿|¥' , '')
munging
```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>3-Jan-16</td>
      <td>1k</td>
      <td>Elderly Couple's Home Burned</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>10-Jan-16</td>
      <td>3k</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
    </tr>
    <tr>
      <th>5</th>
      <td>125</td>
      <td>Veterans &amp; Heroes</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>29-Mar-14</td>
      <td>500</td>
      <td>Raising funds for D-Day Landings Trip</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100</td>
      <td>Travel</td>
      <td>Euro</td>
      <td>1.0</td>
      <td>30-Oct-14</td>
      <td>175</td>
      <td>By my VW</td>
    </tr>
    <tr>
      <th>9</th>
      <td>280</td>
      <td>Sports &amp; Competitions</td>
      <td>Euro</td>
      <td>6.0</td>
      <td>7-Sep-16</td>
      <td>10k</td>
      <td>Help Despina to begin her way to Tokyo 2020</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2,500</td>
      <td>Political fundraising</td>
      <td>Canadian Dollar</td>
      <td>36.0</td>
      <td>7-Sep-16</td>
      <td>2.5k</td>
      <td>Let's get Hilary elected in Ward 2!</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>Legal</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Mar-17</td>
      <td>5k</td>
      <td>Need a miracle of 5k, please help!</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>Health, Illness or Medical</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>3-Mar-18</td>
      <td>500</td>
      <td>Help Marea get Enchroma glasses</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>Family &amp; Kids</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>26-Oct-16</td>
      <td>25k</td>
      <td>Bring Kevin Home to his Family!</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>Faith, Missions &amp; Religion</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>22-Nov-15</td>
      <td>1.6k</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1,765</td>
      <td>Education &amp; Schools</td>
      <td>Singapore Dollar</td>
      <td>14.0</td>
      <td>11-May-17</td>
      <td>10k</td>
      <td>Sri Guru Granth Sahib Ji 3D</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5,110</td>
      <td>Education &amp; Schools</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>10-Nov-17</td>
      <td>5k</td>
      <td>Art Day On-The-Go</td>
    </tr>
    <tr>
      <th>25</th>
      <td>400</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>12.0</td>
      <td>20-Feb-16</td>
      <td>2k</td>
      <td>Gratis dating voor iedereen</td>
    </tr>
    <tr>
      <th>27</th>
      <td>215</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Pound Sterling</td>
      <td>19.0</td>
      <td>9-May-17</td>
      <td>170</td>
      <td>A Tablet for Ablazeko!</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>20-Mar-12</td>
      <td>2k</td>
      <td>Mega Ran's Music Fund</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1,605</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>32.0</td>
      <td>14-Jul-16</td>
      <td>1.8k</td>
      <td>Get Ya Boy Through His Last Year of School</td>
    </tr>
    <tr>
      <th>33</th>
      <td>970</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>24-Sep-14</td>
      <td>25k</td>
      <td>Christian Performing Arts Center Scholarship Fund</td>
    </tr>
    <tr>
      <th>35</th>
      <td>3,083</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>85.0</td>
      <td>4-Apr-15</td>
      <td>5k</td>
      <td>Please help us finish our film, "Mandarava".</td>
    </tr>
    <tr>
      <th>37</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>23-May-17</td>
      <td>25k</td>
      <td>#lovebeatscancer - cancer fundriser May 30th 2017</td>
    </tr>
    <tr>
      <th>39</th>
      <td>450</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>7.0</td>
      <td>17-Mar-17</td>
      <td>4.2k</td>
      <td>Can/USA Early Music Tour with Benjamin Simao 2018</td>
    </tr>
    <tr>
      <th>41</th>
      <td>352</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>25-Mar-14</td>
      <td>1k</td>
      <td>Induct Cheap Trick Petition Campaign</td>
    </tr>
    <tr>
      <th>43</th>
      <td>4,910</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Euro</td>
      <td>33.0</td>
      <td>18-Apr-17</td>
      <td>4k</td>
      <td>Professional Aranea Highwind Project</td>
    </tr>
    <tr>
      <th>45</th>
      <td>830</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>15.0</td>
      <td>25-Apr-17</td>
      <td>5k</td>
      <td>Daughters Of Lilith</td>
    </tr>
    <tr>
      <th>47</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>2.0</td>
      <td>16-Jun-17</td>
      <td>9k</td>
      <td>Help Serbinand say Hello..!</td>
    </tr>
    <tr>
      <th>49</th>
      <td>250</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2-Dec-16</td>
      <td>2.5k</td>
      <td>Statements Dance Company: Black Underground</td>
    </tr>
    <tr>
      <th>51</th>
      <td>697</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>10.0</td>
      <td>10-Feb-16</td>
      <td>3.5k</td>
      <td>Aidez Ben à surpasser ses limites - Help Ben g...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>30,505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Canadian Dollar</td>
      <td>27.0</td>
      <td>22-Feb-16</td>
      <td>30.4k</td>
      <td>Help CubbySpot Get a Government Grant</td>
    </tr>
    <tr>
      <th>55</th>
      <td>200</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Pound Sterling</td>
      <td>1.0</td>
      <td>24-Mar-16</td>
      <td>200</td>
      <td>I wanna crate campaign</td>
    </tr>
    <tr>
      <th>57</th>
      <td>430</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>21-Mar-16</td>
      <td>400</td>
      <td>Nothing's Simple A La Cart</td>
    </tr>
    <tr>
      <th>59</th>
      <td>505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>27-Nov-15</td>
      <td>2.5k</td>
      <td>Lawrence Hines NYC</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3711</th>
      <td>360</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>25-Feb-16</td>
      <td>4.5k</td>
      <td>Please help the refuge of Chios feed rescue dogs</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>140</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>22-Aug-18</td>
      <td>600</td>
      <td>Paw-lease Help, Kaipo Needs Surgery!</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>725</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>25.0</td>
      <td>25-Aug-18</td>
      <td>1k</td>
      <td>Please help us pay for Remy's Parvo expenses.</td>
    </tr>
    <tr>
      <th>3717</th>
      <td>1,000</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>14.0</td>
      <td>25-Jul-18</td>
      <td>2.5k</td>
      <td>Reunite Roxie with her human</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>270</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>19-Aug-18</td>
      <td>680</td>
      <td>Raising Money For Numbi's Oustanding Vet bills</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>430</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>11-Jul-18</td>
      <td>900</td>
      <td>Zara &amp; Zack need help to find their forever homes</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>6,307</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>30-Oct-12</td>
      <td>2k</td>
      <td>Help us help those who can`t ask for help..</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>4.0</td>
      <td>20-Jul-18</td>
      <td>245</td>
      <td>Please support Gray, Nera and Rocky in pension...</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>510</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Oct-13</td>
      <td>5k</td>
      <td>The Silver Lining Fund for Indigent Pets</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>800</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>22.0</td>
      <td>19-Jul-18</td>
      <td>1.5k</td>
      <td>Please help with Buck's medical bill</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>3,719</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>65.0</td>
      <td>3-Jul-18</td>
      <td>7k</td>
      <td>The Voiceless Dogs of Pawtcake refuge July 2018</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>225</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>27-Jul-18</td>
      <td>300</td>
      <td>Help Hermione</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>9-Jul-18</td>
      <td>380</td>
      <td>SURVIVOR, HERO NEEDS HELP TO GET TO HIS NEW HOME</td>
    </tr>
    <tr>
      <th>3737</th>
      <td>254</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>31-Jul-18</td>
      <td>200</td>
      <td>Can We Help this Lady with her Cats and Kittens?</td>
    </tr>
    <tr>
      <th>3739</th>
      <td>938</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>23.0</td>
      <td>25-Jun-18</td>
      <td>1k</td>
      <td>Help for Furries June costs</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1,298</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>16-May-18</td>
      <td>3k</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2,615</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>18-May-18</td>
      <td>3k</td>
      <td>Give us a chance</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>25-Jun-18</td>
      <td>10k</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8,712</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>16-Aug-12</td>
      <td>10k</td>
      <td>Marshall County Animal Shelter</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>11-May-18</td>
      <td>5.5k</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>522</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>11.0</td>
      <td>1-Jun-18</td>
      <td>680</td>
      <td>URGENT!! Food needed for 65 dogs!!!!!!</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>4,724</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>102.0</td>
      <td>9-May-18</td>
      <td>4.5k</td>
      <td>**RAISED** April food for 500 dogs at The Bark...</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8,658</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>6-Jun-18</td>
      <td>7k</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>3-Jul-18</td>
      <td>200</td>
      <td>A016346 needs X-rays on his back leg.</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>187</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>28-Jun-18</td>
      <td>187</td>
      <td>Please help me keep Ralph safe!!!</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Canadian Dollar</td>
      <td>4.0</td>
      <td>10-Jul-18</td>
      <td>900</td>
      <td>Help pay Habiba Shelter's rent and wages July</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>150</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>2.0</td>
      <td>18-Jun-18</td>
      <td>150</td>
      <td>Badly injured tiny kitten needs special care/vet</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>26-May-18</td>
      <td>160</td>
      <td>Help feed 70+ Egyptian rescue dogs for 1 month...</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>425</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>13.0</td>
      <td>3-May-18</td>
      <td>950</td>
      <td>Mildred the Mastín deserves a new start to life.</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>23-Apr-18</td>
      <td>1.3k</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
    </tr>
  </tbody>
</table>
<p>1885 rows × 7 columns</p>
</div>




```python
#convert k and m to zero equivalents
munging['target'] = munging.target.str.replace('k', '000').str.replace('M','0000000').str.replace('Includes|in','')
munging
```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>3-Jan-16</td>
      <td>1000</td>
      <td>Elderly Couple's Home Burned</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>10-Jan-16</td>
      <td>3000</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
    </tr>
    <tr>
      <th>5</th>
      <td>125</td>
      <td>Veterans &amp; Heroes</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>29-Mar-14</td>
      <td>500</td>
      <td>Raising funds for D-Day Landings Trip</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100</td>
      <td>Travel</td>
      <td>Euro</td>
      <td>1.0</td>
      <td>30-Oct-14</td>
      <td>175</td>
      <td>By my VW</td>
    </tr>
    <tr>
      <th>9</th>
      <td>280</td>
      <td>Sports &amp; Competitions</td>
      <td>Euro</td>
      <td>6.0</td>
      <td>7-Sep-16</td>
      <td>10000</td>
      <td>Help Despina to begin her way to Tokyo 2020</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2,500</td>
      <td>Political fundraising</td>
      <td>Canadian Dollar</td>
      <td>36.0</td>
      <td>7-Sep-16</td>
      <td>2.5000</td>
      <td>Let's get Hilary elected in Ward 2!</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>Legal</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Mar-17</td>
      <td>5000</td>
      <td>Need a miracle of 5k, please help!</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>Health, Illness or Medical</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>3-Mar-18</td>
      <td>500</td>
      <td>Help Marea get Enchroma glasses</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>Family &amp; Kids</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>26-Oct-16</td>
      <td>25000</td>
      <td>Bring Kevin Home to his Family!</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>Faith, Missions &amp; Religion</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>22-Nov-15</td>
      <td>1.6000</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1,765</td>
      <td>Education &amp; Schools</td>
      <td>Singapore Dollar</td>
      <td>14.0</td>
      <td>11-May-17</td>
      <td>10000</td>
      <td>Sri Guru Granth Sahib Ji 3D</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5,110</td>
      <td>Education &amp; Schools</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>10-Nov-17</td>
      <td>5000</td>
      <td>Art Day On-The-Go</td>
    </tr>
    <tr>
      <th>25</th>
      <td>400</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>12.0</td>
      <td>20-Feb-16</td>
      <td>2000</td>
      <td>Gratis dating voor iedereen</td>
    </tr>
    <tr>
      <th>27</th>
      <td>215</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Pound Sterling</td>
      <td>19.0</td>
      <td>9-May-17</td>
      <td>170</td>
      <td>A Tablet for Ablazeko!</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>20-Mar-12</td>
      <td>2000</td>
      <td>Mega Ran's Music Fund</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1,605</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>32.0</td>
      <td>14-Jul-16</td>
      <td>1.8000</td>
      <td>Get Ya Boy Through His Last Year of School</td>
    </tr>
    <tr>
      <th>33</th>
      <td>970</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>24-Sep-14</td>
      <td>25000</td>
      <td>Christian Performing Arts Center Scholarship Fund</td>
    </tr>
    <tr>
      <th>35</th>
      <td>3,083</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>85.0</td>
      <td>4-Apr-15</td>
      <td>5000</td>
      <td>Please help us finish our film, "Mandarava".</td>
    </tr>
    <tr>
      <th>37</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>23-May-17</td>
      <td>25000</td>
      <td>#lovebeatscancer - cancer fundriser May 30th 2017</td>
    </tr>
    <tr>
      <th>39</th>
      <td>450</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>7.0</td>
      <td>17-Mar-17</td>
      <td>4.2000</td>
      <td>Can/USA Early Music Tour with Benjamin Simao 2018</td>
    </tr>
    <tr>
      <th>41</th>
      <td>352</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>25-Mar-14</td>
      <td>1000</td>
      <td>Induct Cheap Trick Petition Campaign</td>
    </tr>
    <tr>
      <th>43</th>
      <td>4,910</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Euro</td>
      <td>33.0</td>
      <td>18-Apr-17</td>
      <td>4000</td>
      <td>Professional Aranea Highwind Project</td>
    </tr>
    <tr>
      <th>45</th>
      <td>830</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>15.0</td>
      <td>25-Apr-17</td>
      <td>5000</td>
      <td>Daughters Of Lilith</td>
    </tr>
    <tr>
      <th>47</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>2.0</td>
      <td>16-Jun-17</td>
      <td>9000</td>
      <td>Help Serbinand say Hello..!</td>
    </tr>
    <tr>
      <th>49</th>
      <td>250</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2-Dec-16</td>
      <td>2.5000</td>
      <td>Statements Dance Company: Black Underground</td>
    </tr>
    <tr>
      <th>51</th>
      <td>697</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>10.0</td>
      <td>10-Feb-16</td>
      <td>3.5000</td>
      <td>Aidez Ben à surpasser ses limites - Help Ben g...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>30,505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Canadian Dollar</td>
      <td>27.0</td>
      <td>22-Feb-16</td>
      <td>30.4000</td>
      <td>Help CubbySpot Get a Government Grant</td>
    </tr>
    <tr>
      <th>55</th>
      <td>200</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Pound Sterling</td>
      <td>1.0</td>
      <td>24-Mar-16</td>
      <td>200</td>
      <td>I wanna crate campaign</td>
    </tr>
    <tr>
      <th>57</th>
      <td>430</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>21-Mar-16</td>
      <td>400</td>
      <td>Nothing's Simple A La Cart</td>
    </tr>
    <tr>
      <th>59</th>
      <td>505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>27-Nov-15</td>
      <td>2.5000</td>
      <td>Lawrence Hines NYC</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3711</th>
      <td>360</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>25-Feb-16</td>
      <td>4.5000</td>
      <td>Please help the refuge of Chios feed rescue dogs</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>140</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>22-Aug-18</td>
      <td>600</td>
      <td>Paw-lease Help, Kaipo Needs Surgery!</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>725</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>25.0</td>
      <td>25-Aug-18</td>
      <td>1000</td>
      <td>Please help us pay for Remy's Parvo expenses.</td>
    </tr>
    <tr>
      <th>3717</th>
      <td>1,000</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>14.0</td>
      <td>25-Jul-18</td>
      <td>2.5000</td>
      <td>Reunite Roxie with her human</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>270</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>19-Aug-18</td>
      <td>680</td>
      <td>Raising Money For Numbi's Oustanding Vet bills</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>430</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>11-Jul-18</td>
      <td>900</td>
      <td>Zara &amp; Zack need help to find their forever homes</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>6,307</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>30-Oct-12</td>
      <td>2000</td>
      <td>Help us help those who can`t ask for help..</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>4.0</td>
      <td>20-Jul-18</td>
      <td>245</td>
      <td>Please support Gray, Nera and Rocky in pension...</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>510</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Oct-13</td>
      <td>5000</td>
      <td>The Silver Lining Fund for Indigent Pets</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>800</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>22.0</td>
      <td>19-Jul-18</td>
      <td>1.5000</td>
      <td>Please help with Buck's medical bill</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>3,719</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>65.0</td>
      <td>3-Jul-18</td>
      <td>7000</td>
      <td>The Voiceless Dogs of Pawtcake refuge July 2018</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>225</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>27-Jul-18</td>
      <td>300</td>
      <td>Help Hermione</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>9-Jul-18</td>
      <td>380</td>
      <td>SURVIVOR, HERO NEEDS HELP TO GET TO HIS NEW HOME</td>
    </tr>
    <tr>
      <th>3737</th>
      <td>254</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>31-Jul-18</td>
      <td>200</td>
      <td>Can We Help this Lady with her Cats and Kittens?</td>
    </tr>
    <tr>
      <th>3739</th>
      <td>938</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>23.0</td>
      <td>25-Jun-18</td>
      <td>1000</td>
      <td>Help for Furries June costs</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1,298</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>16-May-18</td>
      <td>3000</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2,615</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>18-May-18</td>
      <td>3000</td>
      <td>Give us a chance</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>25-Jun-18</td>
      <td>10000</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8,712</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>16-Aug-12</td>
      <td>10000</td>
      <td>Marshall County Animal Shelter</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>11-May-18</td>
      <td>5.5000</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>522</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>11.0</td>
      <td>1-Jun-18</td>
      <td>680</td>
      <td>URGENT!! Food needed for 65 dogs!!!!!!</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>4,724</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>102.0</td>
      <td>9-May-18</td>
      <td>4.5000</td>
      <td>**RAISED** April food for 500 dogs at The Bark...</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8,658</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>6-Jun-18</td>
      <td>7000</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>3-Jul-18</td>
      <td>200</td>
      <td>A016346 needs X-rays on his back leg.</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>187</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>28-Jun-18</td>
      <td>187</td>
      <td>Please help me keep Ralph safe!!!</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Canadian Dollar</td>
      <td>4.0</td>
      <td>10-Jul-18</td>
      <td>900</td>
      <td>Help pay Habiba Shelter's rent and wages July</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>150</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>2.0</td>
      <td>18-Jun-18</td>
      <td>150</td>
      <td>Badly injured tiny kitten needs special care/vet</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>26-May-18</td>
      <td>160</td>
      <td>Help feed 70+ Egyptian rescue dogs for 1 month...</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>425</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>13.0</td>
      <td>3-May-18</td>
      <td>950</td>
      <td>Mildred the Mastín deserves a new start to life.</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>23-Apr-18</td>
      <td>1.3000</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
    </tr>
  </tbody>
</table>
<p>1885 rows × 7 columns</p>
</div>




```python
munging['amountraised'] = munging.amountraised.str.replace(',' , '')
munging['target'] = munging.target.str.replace('.', '')
munging
```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>3-Jan-16</td>
      <td>1000</td>
      <td>Elderly Couple's Home Burned</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>10-Jan-16</td>
      <td>3000</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
    </tr>
    <tr>
      <th>5</th>
      <td>125</td>
      <td>Veterans &amp; Heroes</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>29-Mar-14</td>
      <td>500</td>
      <td>Raising funds for D-Day Landings Trip</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100</td>
      <td>Travel</td>
      <td>Euro</td>
      <td>1.0</td>
      <td>30-Oct-14</td>
      <td>175</td>
      <td>By my VW</td>
    </tr>
    <tr>
      <th>9</th>
      <td>280</td>
      <td>Sports &amp; Competitions</td>
      <td>Euro</td>
      <td>6.0</td>
      <td>7-Sep-16</td>
      <td>10000</td>
      <td>Help Despina to begin her way to Tokyo 2020</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2500</td>
      <td>Political fundraising</td>
      <td>Canadian Dollar</td>
      <td>36.0</td>
      <td>7-Sep-16</td>
      <td>25000</td>
      <td>Let's get Hilary elected in Ward 2!</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>Legal</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Mar-17</td>
      <td>5000</td>
      <td>Need a miracle of 5k, please help!</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>Health, Illness or Medical</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>3-Mar-18</td>
      <td>500</td>
      <td>Help Marea get Enchroma glasses</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>Family &amp; Kids</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>26-Oct-16</td>
      <td>25000</td>
      <td>Bring Kevin Home to his Family!</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>Faith, Missions &amp; Religion</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>22-Nov-15</td>
      <td>16000</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1765</td>
      <td>Education &amp; Schools</td>
      <td>Singapore Dollar</td>
      <td>14.0</td>
      <td>11-May-17</td>
      <td>10000</td>
      <td>Sri Guru Granth Sahib Ji 3D</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5110</td>
      <td>Education &amp; Schools</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>10-Nov-17</td>
      <td>5000</td>
      <td>Art Day On-The-Go</td>
    </tr>
    <tr>
      <th>25</th>
      <td>400</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>12.0</td>
      <td>20-Feb-16</td>
      <td>2000</td>
      <td>Gratis dating voor iedereen</td>
    </tr>
    <tr>
      <th>27</th>
      <td>215</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Pound Sterling</td>
      <td>19.0</td>
      <td>9-May-17</td>
      <td>170</td>
      <td>A Tablet for Ablazeko!</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>20-Mar-12</td>
      <td>2000</td>
      <td>Mega Ran's Music Fund</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1605</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>32.0</td>
      <td>14-Jul-16</td>
      <td>18000</td>
      <td>Get Ya Boy Through His Last Year of School</td>
    </tr>
    <tr>
      <th>33</th>
      <td>970</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>24-Sep-14</td>
      <td>25000</td>
      <td>Christian Performing Arts Center Scholarship Fund</td>
    </tr>
    <tr>
      <th>35</th>
      <td>3083</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>85.0</td>
      <td>4-Apr-15</td>
      <td>5000</td>
      <td>Please help us finish our film, "Mandarava".</td>
    </tr>
    <tr>
      <th>37</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>23-May-17</td>
      <td>25000</td>
      <td>#lovebeatscancer - cancer fundriser May 30th 2017</td>
    </tr>
    <tr>
      <th>39</th>
      <td>450</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>7.0</td>
      <td>17-Mar-17</td>
      <td>42000</td>
      <td>Can/USA Early Music Tour with Benjamin Simao 2018</td>
    </tr>
    <tr>
      <th>41</th>
      <td>352</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>25-Mar-14</td>
      <td>1000</td>
      <td>Induct Cheap Trick Petition Campaign</td>
    </tr>
    <tr>
      <th>43</th>
      <td>4910</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Euro</td>
      <td>33.0</td>
      <td>18-Apr-17</td>
      <td>4000</td>
      <td>Professional Aranea Highwind Project</td>
    </tr>
    <tr>
      <th>45</th>
      <td>830</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>15.0</td>
      <td>25-Apr-17</td>
      <td>5000</td>
      <td>Daughters Of Lilith</td>
    </tr>
    <tr>
      <th>47</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>Canadian Dollar</td>
      <td>2.0</td>
      <td>16-Jun-17</td>
      <td>9000</td>
      <td>Help Serbinand say Hello..!</td>
    </tr>
    <tr>
      <th>49</th>
      <td>250</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2-Dec-16</td>
      <td>25000</td>
      <td>Statements Dance Company: Black Underground</td>
    </tr>
    <tr>
      <th>51</th>
      <td>697</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Euro</td>
      <td>10.0</td>
      <td>10-Feb-16</td>
      <td>35000</td>
      <td>Aidez Ben à surpasser ses limites - Help Ben g...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>30505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Canadian Dollar</td>
      <td>27.0</td>
      <td>22-Feb-16</td>
      <td>304000</td>
      <td>Help CubbySpot Get a Government Grant</td>
    </tr>
    <tr>
      <th>55</th>
      <td>200</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>Pound Sterling</td>
      <td>1.0</td>
      <td>24-Mar-16</td>
      <td>200</td>
      <td>I wanna crate campaign</td>
    </tr>
    <tr>
      <th>57</th>
      <td>430</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>21-Mar-16</td>
      <td>400</td>
      <td>Nothing's Simple A La Cart</td>
    </tr>
    <tr>
      <th>59</th>
      <td>505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>27-Nov-15</td>
      <td>25000</td>
      <td>Lawrence Hines NYC</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3711</th>
      <td>360</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>25-Feb-16</td>
      <td>45000</td>
      <td>Please help the refuge of Chios feed rescue dogs</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>140</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>22-Aug-18</td>
      <td>600</td>
      <td>Paw-lease Help, Kaipo Needs Surgery!</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>725</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>25.0</td>
      <td>25-Aug-18</td>
      <td>1000</td>
      <td>Please help us pay for Remy's Parvo expenses.</td>
    </tr>
    <tr>
      <th>3717</th>
      <td>1000</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>14.0</td>
      <td>25-Jul-18</td>
      <td>25000</td>
      <td>Reunite Roxie with her human</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>270</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>19-Aug-18</td>
      <td>680</td>
      <td>Raising Money For Numbi's Oustanding Vet bills</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>430</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>11-Jul-18</td>
      <td>900</td>
      <td>Zara &amp; Zack need help to find their forever homes</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>6307</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>30-Oct-12</td>
      <td>2000</td>
      <td>Help us help those who can`t ask for help..</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>4.0</td>
      <td>20-Jul-18</td>
      <td>245</td>
      <td>Please support Gray, Nera and Rocky in pension...</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>510</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>25-Oct-13</td>
      <td>5000</td>
      <td>The Silver Lining Fund for Indigent Pets</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>800</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>22.0</td>
      <td>19-Jul-18</td>
      <td>15000</td>
      <td>Please help with Buck's medical bill</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>3719</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>65.0</td>
      <td>3-Jul-18</td>
      <td>7000</td>
      <td>The Voiceless Dogs of Pawtcake refuge July 2018</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>225</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>27-Jul-18</td>
      <td>300</td>
      <td>Help Hermione</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>9-Jul-18</td>
      <td>380</td>
      <td>SURVIVOR, HERO NEEDS HELP TO GET TO HIS NEW HOME</td>
    </tr>
    <tr>
      <th>3737</th>
      <td>254</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>31-Jul-18</td>
      <td>200</td>
      <td>Can We Help this Lady with her Cats and Kittens?</td>
    </tr>
    <tr>
      <th>3739</th>
      <td>938</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>23.0</td>
      <td>25-Jun-18</td>
      <td>1000</td>
      <td>Help for Furries June costs</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1298</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>16-May-18</td>
      <td>3000</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2615</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>18-May-18</td>
      <td>3000</td>
      <td>Give us a chance</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>25-Jun-18</td>
      <td>10000</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8712</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>16-Aug-12</td>
      <td>10000</td>
      <td>Marshall County Animal Shelter</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>11-May-18</td>
      <td>55000</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
    </tr>
    <tr>
      <th>3751</th>
      <td>522</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>11.0</td>
      <td>1-Jun-18</td>
      <td>680</td>
      <td>URGENT!! Food needed for 65 dogs!!!!!!</td>
    </tr>
    <tr>
      <th>3753</th>
      <td>4724</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>102.0</td>
      <td>9-May-18</td>
      <td>45000</td>
      <td>**RAISED** April food for 500 dogs at The Bark...</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8658</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>6-Jun-18</td>
      <td>7000</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>3-Jul-18</td>
      <td>200</td>
      <td>A016346 needs X-rays on his back leg.</td>
    </tr>
    <tr>
      <th>3759</th>
      <td>187</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>5.0</td>
      <td>28-Jun-18</td>
      <td>187</td>
      <td>Please help me keep Ralph safe!!!</td>
    </tr>
    <tr>
      <th>3761</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Canadian Dollar</td>
      <td>4.0</td>
      <td>10-Jul-18</td>
      <td>900</td>
      <td>Help pay Habiba Shelter's rent and wages July</td>
    </tr>
    <tr>
      <th>3763</th>
      <td>150</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>2.0</td>
      <td>18-Jun-18</td>
      <td>150</td>
      <td>Badly injured tiny kitten needs special care/vet</td>
    </tr>
    <tr>
      <th>3765</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Pound Sterling</td>
      <td>9.0</td>
      <td>26-May-18</td>
      <td>160</td>
      <td>Help feed 70+ Egyptian rescue dogs for 1 month...</td>
    </tr>
    <tr>
      <th>3767</th>
      <td>425</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>Euro</td>
      <td>13.0</td>
      <td>3-May-18</td>
      <td>950</td>
      <td>Mildred the Mastín deserves a new start to life.</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>23-Apr-18</td>
      <td>13000</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
    </tr>
  </tbody>
</table>
<p>1885 rows × 7 columns</p>
</div>






```python
#change amount raised to numeric datatype
munging['amountraised'] = pd.to_numeric(munging['amountraised'])

munging['target'] = pd.to_numeric(munging['target'])
```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.
    


```python
#get date from today and subtract from start date to get total days campaign has been open
import datetime
munging['startDate'] = pd.to_datetime(munging['startDate'])
munging['today'] = pd.Timestamp('20181013')
munging['days'] = (munging['today'] - munging['startDate']).dt.days
munging['days'] = pd.to_numeric(munging['days'])
```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    


```python
#create two new columns average contribution per person and percent_completed to target amount
munging['averagecontribution'] = munging['amountraised'] / munging['numbercontributors']
munging['percent_complt'] = (munging['amountraised']/ munging['target']) * 100
munging['percent_complt'] = pd.to_numeric(munging['percent_complt'])
munging ['percent_complt'] = round(munging['percent_complt'],0)

```

    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.
    C:\Users\rajes\Anaconda4\lib\site-packages\ipykernel_launcher.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """
    


```python
#update dataframe with rows that have only U.S Dollar
from matplotlib import pyplot as plt
plt.style.use('ggplot')
munging = munging[munging.currencyused == 'U.S. Dollar']
munging
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amountraised</th>
      <th>category</th>
      <th>currencyused</th>
      <th>numbercontributors</th>
      <th>startDate</th>
      <th>target</th>
      <th>title</th>
      <th>today</th>
      <th>days</th>
      <th>averagecontribution</th>
      <th>percent_complt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>892</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>2016-01-03</td>
      <td>1000</td>
      <td>Elderly Couple's Home Burned</td>
      <td>2018-10-13</td>
      <td>1014</td>
      <td>59.466667</td>
      <td>89.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>125</td>
      <td>Accidents &amp; Disasters</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>2016-01-10</td>
      <td>3000</td>
      <td>Abram and Brandy's son Kamren Needs Mom and Dad!</td>
      <td>2018-10-13</td>
      <td>1007</td>
      <td>62.500000</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>735</td>
      <td>Legal</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>2017-03-25</td>
      <td>5000</td>
      <td>Need a miracle of 5k, please help!</td>
      <td>2018-10-13</td>
      <td>567</td>
      <td>49.000000</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>500</td>
      <td>Health, Illness or Medical</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>2018-03-03</td>
      <td>500</td>
      <td>Help Marea get Enchroma glasses</td>
      <td>2018-10-13</td>
      <td>224</td>
      <td>45.454545</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>240</td>
      <td>Family &amp; Kids</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>2016-10-26</td>
      <td>25000</td>
      <td>Bring Kevin Home to his Family!</td>
      <td>2018-10-13</td>
      <td>717</td>
      <td>48.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>701</td>
      <td>Faith, Missions &amp; Religion</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>2015-11-22</td>
      <td>16000</td>
      <td>Kevin McAfee's 2016 Trip to Haiti</td>
      <td>2018-10-13</td>
      <td>1056</td>
      <td>87.625000</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5110</td>
      <td>Education &amp; Schools</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>2017-11-10</td>
      <td>5000</td>
      <td>Art Day On-The-Go</td>
      <td>2018-10-13</td>
      <td>337</td>
      <td>730.000000</td>
      <td>102.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>616</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>23.0</td>
      <td>2012-03-20</td>
      <td>2000</td>
      <td>Mega Ran's Music Fund</td>
      <td>2018-10-13</td>
      <td>2398</td>
      <td>26.782609</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1605</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>32.0</td>
      <td>2016-07-14</td>
      <td>18000</td>
      <td>Get Ya Boy Through His Last Year of School</td>
      <td>2018-10-13</td>
      <td>821</td>
      <td>50.156250</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>970</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>2014-09-24</td>
      <td>25000</td>
      <td>Christian Performing Arts Center Scholarship Fund</td>
      <td>2018-10-13</td>
      <td>1480</td>
      <td>97.000000</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>3083</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>85.0</td>
      <td>2015-04-04</td>
      <td>5000</td>
      <td>Please help us finish our film, "Mandarava".</td>
      <td>2018-10-13</td>
      <td>1288</td>
      <td>36.270588</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>100</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>2017-05-23</td>
      <td>25000</td>
      <td>#lovebeatscancer - cancer fundriser May 30th 2017</td>
      <td>2018-10-13</td>
      <td>508</td>
      <td>50.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>352</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>10.0</td>
      <td>2014-03-25</td>
      <td>1000</td>
      <td>Induct Cheap Trick Petition Campaign</td>
      <td>2018-10-13</td>
      <td>1663</td>
      <td>35.200000</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>250</td>
      <td>Arts, Creative &amp; Fashion</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2016-12-02</td>
      <td>25000</td>
      <td>Statements Dance Company: Black Underground</td>
      <td>2018-10-13</td>
      <td>680</td>
      <td>41.666667</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>430</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>2016-03-21</td>
      <td>400</td>
      <td>Nothing's Simple A La Cart</td>
      <td>2018-10-13</td>
      <td>936</td>
      <td>33.076923</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>505</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>2015-11-27</td>
      <td>25000</td>
      <td>Lawrence Hines NYC</td>
      <td>2018-10-13</td>
      <td>1051</td>
      <td>56.111111</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>67</th>
      <td>1767</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>37.0</td>
      <td>2016-03-11</td>
      <td>5000</td>
      <td>Mama Bear &amp; Cub- Giving Mothers &amp; Families opt...</td>
      <td>2018-10-13</td>
      <td>946</td>
      <td>47.756757</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>69</th>
      <td>125</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>2016-01-28</td>
      <td>15000</td>
      <td>Help The Flour Dog Grow Our Commercial Kitchen!</td>
      <td>2018-10-13</td>
      <td>989</td>
      <td>125.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>71</th>
      <td>150</td>
      <td>Business &amp; Entrepreneurial</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>2016-04-14</td>
      <td>5000</td>
      <td>Junior Entrepreneurs</td>
      <td>2018-10-13</td>
      <td>912</td>
      <td>75.000000</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>73</th>
      <td>365</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>17.0</td>
      <td>2014-12-20</td>
      <td>500</td>
      <td>A SMALL REQUEST FOR A BIG CAUSE!</td>
      <td>2018-10-13</td>
      <td>1393</td>
      <td>21.470588</td>
      <td>73.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>465</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>19.0</td>
      <td>2014-10-10</td>
      <td>10000</td>
      <td>Worlds Oldest Professional Poker Dealer USA</td>
      <td>2018-10-13</td>
      <td>1464</td>
      <td>24.473684</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>235</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>2014-12-23</td>
      <td>15000</td>
      <td>2015 Paramount Chief Adv. Vekuii Rukoro's US V...</td>
      <td>2018-10-13</td>
      <td>1390</td>
      <td>33.571429</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>766</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>2014-12-30</td>
      <td>2000</td>
      <td>Help Throw a Kick-Ass 50th Birthday for Cather...</td>
      <td>2018-10-13</td>
      <td>1383</td>
      <td>28.370370</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>81</th>
      <td>4670</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>58.0</td>
      <td>2015-01-01</td>
      <td>5000</td>
      <td>Support Appreciation Fund Raise</td>
      <td>2018-10-13</td>
      <td>1381</td>
      <td>80.517241</td>
      <td>93.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>100</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>2015-01-26</td>
      <td>2000</td>
      <td>Help Us Have Our Dream Wedding</td>
      <td>2018-10-13</td>
      <td>1356</td>
      <td>100.000000</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>350</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>2014-11-23</td>
      <td>3000</td>
      <td>Steph and I are getting Married</td>
      <td>2018-10-13</td>
      <td>1420</td>
      <td>116.666667</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>87</th>
      <td>500</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>2015-02-04</td>
      <td>2000</td>
      <td>Trip to Mexico</td>
      <td>2018-10-13</td>
      <td>1347</td>
      <td>500.000000</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>89</th>
      <td>150</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>2014-03-06</td>
      <td>980</td>
      <td>Tasha's Bachelorette Party 2015</td>
      <td>2018-10-13</td>
      <td>1682</td>
      <td>50.000000</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>500</td>
      <td>Celebrations &amp; Weddings</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>2014-02-19</td>
      <td>500</td>
      <td>Become a Titled Member of the Krewe Of Fools</td>
      <td>2018-10-13</td>
      <td>1697</td>
      <td>33.333333</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>4516</td>
      <td>Community &amp; Volunteer</td>
      <td>U.S. Dollar</td>
      <td>149.0</td>
      <td>2018-04-19</td>
      <td>15000</td>
      <td>Recalibrate: TTEOTS Micro Art Fundrazr</td>
      <td>2018-10-13</td>
      <td>177</td>
      <td>30.308725</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3663</th>
      <td>435</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>9.0</td>
      <td>2018-09-06</td>
      <td>1000</td>
      <td>Pablo's Smile Fund</td>
      <td>2018-10-13</td>
      <td>37</td>
      <td>48.333333</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>3667</th>
      <td>3855</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>42.0</td>
      <td>2018-08-15</td>
      <td>6000</td>
      <td>Help LEO Africa buy new camera traps</td>
      <td>2018-10-13</td>
      <td>59</td>
      <td>91.785714</td>
      <td>64.0</td>
    </tr>
    <tr>
      <th>3673</th>
      <td>155</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>2018-09-09</td>
      <td>284</td>
      <td>Please help us pay this neglected dogs vet bill</td>
      <td>2018-10-13</td>
      <td>34</td>
      <td>31.000000</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>3679</th>
      <td>470</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2018-09-14</td>
      <td>460</td>
      <td>A017482 has a fractured femur</td>
      <td>2018-10-13</td>
      <td>29</td>
      <td>78.333333</td>
      <td>102.0</td>
    </tr>
    <tr>
      <th>3689</th>
      <td>23362</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>560.0</td>
      <td>2013-02-08</td>
      <td>30000</td>
      <td>100+ Abandoned Dogs of Everglades Florida</td>
      <td>2018-10-13</td>
      <td>2073</td>
      <td>41.717857</td>
      <td>78.0</td>
    </tr>
    <tr>
      <th>3693</th>
      <td>185</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>2018-08-31</td>
      <td>15000</td>
      <td>Will YOU help SAVE ME ....</td>
      <td>2018-10-13</td>
      <td>43</td>
      <td>37.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3695</th>
      <td>160</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>2018-06-07</td>
      <td>450</td>
      <td>Pike's Heartworm Treatment</td>
      <td>2018-10-13</td>
      <td>128</td>
      <td>40.000000</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>3697</th>
      <td>1242</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>18.0</td>
      <td>2016-12-18</td>
      <td>2000</td>
      <td>Help Chella to save her Animal Refuge</td>
      <td>2018-10-13</td>
      <td>664</td>
      <td>69.000000</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>3699</th>
      <td>300</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>2018-08-24</td>
      <td>1000</td>
      <td>Please Help Me Save Adrienne</td>
      <td>2018-10-13</td>
      <td>50</td>
      <td>37.500000</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>3703</th>
      <td>265</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>8.0</td>
      <td>2018-05-31</td>
      <td>360</td>
      <td>A015860 needs to be boarded while he heals.</td>
      <td>2018-10-13</td>
      <td>135</td>
      <td>33.125000</td>
      <td>74.0</td>
    </tr>
    <tr>
      <th>3705</th>
      <td>110</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>2018-06-05</td>
      <td>485</td>
      <td>A015890, her bill is due, please donate if you...</td>
      <td>2018-10-13</td>
      <td>130</td>
      <td>27.500000</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>3709</th>
      <td>1230</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>13.0</td>
      <td>2018-08-06</td>
      <td>33000</td>
      <td>Mattie's Amputation for Life</td>
      <td>2018-10-13</td>
      <td>68</td>
      <td>94.615385</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>140</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>6.0</td>
      <td>2018-08-22</td>
      <td>600</td>
      <td>Paw-lease Help, Kaipo Needs Surgery!</td>
      <td>2018-10-13</td>
      <td>52</td>
      <td>23.333333</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>725</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>25.0</td>
      <td>2018-08-25</td>
      <td>1000</td>
      <td>Please help us pay for Remy's Parvo expenses.</td>
      <td>2018-10-13</td>
      <td>49</td>
      <td>29.000000</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>270</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>3.0</td>
      <td>2018-08-19</td>
      <td>680</td>
      <td>Raising Money For Numbi's Oustanding Vet bills</td>
      <td>2018-10-13</td>
      <td>55</td>
      <td>90.000000</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>430</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>2018-07-11</td>
      <td>900</td>
      <td>Zara &amp; Zack need help to find their forever homes</td>
      <td>2018-10-13</td>
      <td>94</td>
      <td>86.000000</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>6307</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>27.0</td>
      <td>2012-10-30</td>
      <td>2000</td>
      <td>Help us help those who can`t ask for help..</td>
      <td>2018-10-13</td>
      <td>2174</td>
      <td>233.592593</td>
      <td>315.0</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>510</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>15.0</td>
      <td>2013-10-25</td>
      <td>5000</td>
      <td>The Silver Lining Fund for Indigent Pets</td>
      <td>2018-10-13</td>
      <td>1814</td>
      <td>34.000000</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>800</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>22.0</td>
      <td>2018-07-19</td>
      <td>15000</td>
      <td>Please help with Buck's medical bill</td>
      <td>2018-10-13</td>
      <td>86</td>
      <td>36.363636</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>3719</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>65.0</td>
      <td>2018-07-03</td>
      <td>7000</td>
      <td>The Voiceless Dogs of Pawtcake refuge July 2018</td>
      <td>2018-10-13</td>
      <td>102</td>
      <td>57.215385</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>225</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>7.0</td>
      <td>2018-07-27</td>
      <td>300</td>
      <td>Help Hermione</td>
      <td>2018-10-13</td>
      <td>78</td>
      <td>32.142857</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>5.0</td>
      <td>2018-07-09</td>
      <td>380</td>
      <td>SURVIVOR, HERO NEEDS HELP TO GET TO HIS NEW HOME</td>
      <td>2018-10-13</td>
      <td>96</td>
      <td>48.000000</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>1298</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>48.0</td>
      <td>2018-05-16</td>
      <td>3000</td>
      <td>URGENT HELP FOR COSTA!!!!</td>
      <td>2018-10-13</td>
      <td>150</td>
      <td>27.041667</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>2615</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>128.0</td>
      <td>2018-05-18</td>
      <td>3000</td>
      <td>Give us a chance</td>
      <td>2018-10-13</td>
      <td>148</td>
      <td>20.429688</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>100</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>1.0</td>
      <td>2018-06-25</td>
      <td>10000</td>
      <td>AnimalLoversUnite-AWholesale pet food buying g...</td>
      <td>2018-10-13</td>
      <td>110</td>
      <td>100.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>8712</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>206.0</td>
      <td>2012-08-16</td>
      <td>10000</td>
      <td>Marshall County Animal Shelter</td>
      <td>2018-10-13</td>
      <td>2249</td>
      <td>42.291262</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>120</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>2.0</td>
      <td>2018-05-11</td>
      <td>55000</td>
      <td>Help For Bella and her fight for Xiytol Toxicity</td>
      <td>2018-10-13</td>
      <td>155</td>
      <td>60.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>8658</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>76.0</td>
      <td>2018-06-06</td>
      <td>7000</td>
      <td>The Voiceless Dogs of Pawtcake Refuge June 2018</td>
      <td>2018-10-13</td>
      <td>129</td>
      <td>113.921053</td>
      <td>124.0</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>240</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>4.0</td>
      <td>2018-07-03</td>
      <td>200</td>
      <td>A016346 needs X-rays on his back leg.</td>
      <td>2018-10-13</td>
      <td>102</td>
      <td>60.000000</td>
      <td>120.0</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>950</td>
      <td>Animals, Pets &amp; Humane</td>
      <td>U.S. Dollar</td>
      <td>11.0</td>
      <td>2018-04-23</td>
      <td>13000</td>
      <td>Please Help Us Support Dog Meat Trade Survivors</td>
      <td>2018-10-13</td>
      <td>173</td>
      <td>86.363636</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
<p>1357 rows × 11 columns</p>
</div>




```python
#create new dataframe from old dataframe munging and the new columns days, averagecontribution, and percent_complt
data = pd.concat([munging['category'],munging['averagecontribution'],munging['percent_complt'], munging['currencyused'], munging['days'],munging['target'], munging['amountraised'],munging['numbercontributors']], axis = 1, keys=['category', 'averagecontribution','percent_complt', 'currencyused','days','target','amountraised', 'numbercontributors'])
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>averagecontribution</th>
      <th>percent_complt</th>
      <th>currencyused</th>
      <th>days</th>
      <th>target</th>
      <th>amountraised</th>
      <th>numbercontributors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Accidents &amp; Disasters</td>
      <td>59.466667</td>
      <td>89.0</td>
      <td>U.S. Dollar</td>
      <td>1014</td>
      <td>1000</td>
      <td>892</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Accidents &amp; Disasters</td>
      <td>62.500000</td>
      <td>4.0</td>
      <td>U.S. Dollar</td>
      <td>1007</td>
      <td>3000</td>
      <td>125</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Legal</td>
      <td>49.000000</td>
      <td>15.0</td>
      <td>U.S. Dollar</td>
      <td>567</td>
      <td>5000</td>
      <td>735</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Health, Illness or Medical</td>
      <td>45.454545</td>
      <td>100.0</td>
      <td>U.S. Dollar</td>
      <td>224</td>
      <td>500</td>
      <td>500</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Family &amp; Kids</td>
      <td>48.000000</td>
      <td>1.0</td>
      <td>U.S. Dollar</td>
      <td>717</td>
      <td>25000</td>
      <td>240</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Faith, Missions &amp; Religion</td>
      <td>87.625000</td>
      <td>4.0</td>
      <td>U.S. Dollar</td>
      <td>1056</td>
      <td>16000</td>
      <td>701</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Education &amp; Schools</td>
      <td>730.000000</td>
      <td>102.0</td>
      <td>U.S. Dollar</td>
      <td>337</td>
      <td>5000</td>
      <td>5110</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Arts, Creative &amp; Fashion</td>
      <td>26.782609</td>
      <td>31.0</td>
      <td>U.S. Dollar</td>
      <td>2398</td>
      <td>2000</td>
      <td>616</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Arts, Creative &amp; Fashion</td>
      <td>50.156250</td>
      <td>9.0</td>
      <td>U.S. Dollar</td>
      <td>821</td>
      <td>18000</td>
      <td>1605</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Arts, Creative &amp; Fashion</td>
      <td>97.000000</td>
      <td>4.0</td>
      <td>U.S. Dollar</td>
      <td>1480</td>
      <td>25000</td>
      <td>970</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Arts, Creative &amp; Fashion</td>
      <td>36.270588</td>
      <td>62.0</td>
      <td>U.S. Dollar</td>
      <td>1288</td>
      <td>5000</td>
      <td>3083</td>
      <td>85.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Arts, Creative &amp; Fashion</td>
      <td>50.000000</td>
      <td>0.0</td>
      <td>U.S. Dollar</td>
      <td>508</td>
      <td>25000</td>
      <td>100</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Arts, Creative &amp; Fashion</td>
      <td>35.200000</td>
      <td>35.0</td>
      <td>U.S. Dollar</td>
      <td>1663</td>
      <td>1000</td>
      <td>352</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Arts, Creative &amp; Fashion</td>
      <td>41.666667</td>
      <td>1.0</td>
      <td>U.S. Dollar</td>
      <td>680</td>
      <td>25000</td>
      <td>250</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Business &amp; Entrepreneurial</td>
      <td>33.076923</td>
      <td>108.0</td>
      <td>U.S. Dollar</td>
      <td>936</td>
      <td>400</td>
      <td>430</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Business &amp; Entrepreneurial</td>
      <td>56.111111</td>
      <td>2.0</td>
      <td>U.S. Dollar</td>
      <td>1051</td>
      <td>25000</td>
      <td>505</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Business &amp; Entrepreneurial</td>
      <td>47.756757</td>
      <td>35.0</td>
      <td>U.S. Dollar</td>
      <td>946</td>
      <td>5000</td>
      <td>1767</td>
      <td>37.0</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Business &amp; Entrepreneurial</td>
      <td>125.000000</td>
      <td>1.0</td>
      <td>U.S. Dollar</td>
      <td>989</td>
      <td>15000</td>
      <td>125</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Business &amp; Entrepreneurial</td>
      <td>75.000000</td>
      <td>3.0</td>
      <td>U.S. Dollar</td>
      <td>912</td>
      <td>5000</td>
      <td>150</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Celebrations &amp; Weddings</td>
      <td>21.470588</td>
      <td>73.0</td>
      <td>U.S. Dollar</td>
      <td>1393</td>
      <td>500</td>
      <td>365</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Celebrations &amp; Weddings</td>
      <td>24.473684</td>
      <td>5.0</td>
      <td>U.S. Dollar</td>
      <td>1464</td>
      <td>10000</td>
      <td>465</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Celebrations &amp; Weddings</td>
      <td>33.571429</td>
      <td>2.0</td>
      <td>U.S. Dollar</td>
      <td>1390</td>
      <td>15000</td>
      <td>235</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Celebrations &amp; Weddings</td>
      <td>28.370370</td>
      <td>38.0</td>
      <td>U.S. Dollar</td>
      <td>1383</td>
      <td>2000</td>
      <td>766</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Celebrations &amp; Weddings</td>
      <td>80.517241</td>
      <td>93.0</td>
      <td>U.S. Dollar</td>
      <td>1381</td>
      <td>5000</td>
      <td>4670</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Celebrations &amp; Weddings</td>
      <td>100.000000</td>
      <td>5.0</td>
      <td>U.S. Dollar</td>
      <td>1356</td>
      <td>2000</td>
      <td>100</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Celebrations &amp; Weddings</td>
      <td>116.666667</td>
      <td>12.0</td>
      <td>U.S. Dollar</td>
      <td>1420</td>
      <td>3000</td>
      <td>350</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Celebrations &amp; Weddings</td>
      <td>500.000000</td>
      <td>25.0</td>
      <td>U.S. Dollar</td>
      <td>1347</td>
      <td>2000</td>
      <td>500</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Celebrations &amp; Weddings</td>
      <td>50.000000</td>
      <td>15.0</td>
      <td>U.S. Dollar</td>
      <td>1682</td>
      <td>980</td>
      <td>150</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Celebrations &amp; Weddings</td>
      <td>33.333333</td>
      <td>100.0</td>
      <td>U.S. Dollar</td>
      <td>1697</td>
      <td>500</td>
      <td>500</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Community &amp; Volunteer</td>
      <td>30.308725</td>
      <td>30.0</td>
      <td>U.S. Dollar</td>
      <td>177</td>
      <td>15000</td>
      <td>4516</td>
      <td>149.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3663</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>48.333333</td>
      <td>44.0</td>
      <td>U.S. Dollar</td>
      <td>37</td>
      <td>1000</td>
      <td>435</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>3667</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>91.785714</td>
      <td>64.0</td>
      <td>U.S. Dollar</td>
      <td>59</td>
      <td>6000</td>
      <td>3855</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>3673</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>31.000000</td>
      <td>55.0</td>
      <td>U.S. Dollar</td>
      <td>34</td>
      <td>284</td>
      <td>155</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3679</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>78.333333</td>
      <td>102.0</td>
      <td>U.S. Dollar</td>
      <td>29</td>
      <td>460</td>
      <td>470</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3689</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>41.717857</td>
      <td>78.0</td>
      <td>U.S. Dollar</td>
      <td>2073</td>
      <td>30000</td>
      <td>23362</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th>3693</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>37.000000</td>
      <td>1.0</td>
      <td>U.S. Dollar</td>
      <td>43</td>
      <td>15000</td>
      <td>185</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3695</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>40.000000</td>
      <td>36.0</td>
      <td>U.S. Dollar</td>
      <td>128</td>
      <td>450</td>
      <td>160</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3697</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>69.000000</td>
      <td>62.0</td>
      <td>U.S. Dollar</td>
      <td>664</td>
      <td>2000</td>
      <td>1242</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>3699</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>37.500000</td>
      <td>30.0</td>
      <td>U.S. Dollar</td>
      <td>50</td>
      <td>1000</td>
      <td>300</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3703</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>33.125000</td>
      <td>74.0</td>
      <td>U.S. Dollar</td>
      <td>135</td>
      <td>360</td>
      <td>265</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3705</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>27.500000</td>
      <td>23.0</td>
      <td>U.S. Dollar</td>
      <td>130</td>
      <td>485</td>
      <td>110</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3709</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>94.615385</td>
      <td>4.0</td>
      <td>U.S. Dollar</td>
      <td>68</td>
      <td>33000</td>
      <td>1230</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>3713</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>23.333333</td>
      <td>23.0</td>
      <td>U.S. Dollar</td>
      <td>52</td>
      <td>600</td>
      <td>140</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3715</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>29.000000</td>
      <td>72.0</td>
      <td>U.S. Dollar</td>
      <td>49</td>
      <td>1000</td>
      <td>725</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>90.000000</td>
      <td>40.0</td>
      <td>U.S. Dollar</td>
      <td>55</td>
      <td>680</td>
      <td>270</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>86.000000</td>
      <td>48.0</td>
      <td>U.S. Dollar</td>
      <td>94</td>
      <td>900</td>
      <td>430</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>233.592593</td>
      <td>315.0</td>
      <td>U.S. Dollar</td>
      <td>2174</td>
      <td>2000</td>
      <td>6307</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>3727</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>34.000000</td>
      <td>10.0</td>
      <td>U.S. Dollar</td>
      <td>1814</td>
      <td>5000</td>
      <td>510</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>36.363636</td>
      <td>5.0</td>
      <td>U.S. Dollar</td>
      <td>86</td>
      <td>15000</td>
      <td>800</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>3731</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>57.215385</td>
      <td>53.0</td>
      <td>U.S. Dollar</td>
      <td>102</td>
      <td>7000</td>
      <td>3719</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>32.142857</td>
      <td>75.0</td>
      <td>U.S. Dollar</td>
      <td>78</td>
      <td>300</td>
      <td>225</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3735</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>48.000000</td>
      <td>63.0</td>
      <td>U.S. Dollar</td>
      <td>96</td>
      <td>380</td>
      <td>240</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3741</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>27.041667</td>
      <td>43.0</td>
      <td>U.S. Dollar</td>
      <td>150</td>
      <td>3000</td>
      <td>1298</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>3743</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>20.429688</td>
      <td>87.0</td>
      <td>U.S. Dollar</td>
      <td>148</td>
      <td>3000</td>
      <td>2615</td>
      <td>128.0</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>100.000000</td>
      <td>1.0</td>
      <td>U.S. Dollar</td>
      <td>110</td>
      <td>10000</td>
      <td>100</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3747</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>42.291262</td>
      <td>87.0</td>
      <td>U.S. Dollar</td>
      <td>2249</td>
      <td>10000</td>
      <td>8712</td>
      <td>206.0</td>
    </tr>
    <tr>
      <th>3749</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>60.000000</td>
      <td>0.0</td>
      <td>U.S. Dollar</td>
      <td>155</td>
      <td>55000</td>
      <td>120</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3755</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>113.921053</td>
      <td>124.0</td>
      <td>U.S. Dollar</td>
      <td>129</td>
      <td>7000</td>
      <td>8658</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>3757</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>60.000000</td>
      <td>120.0</td>
      <td>U.S. Dollar</td>
      <td>102</td>
      <td>200</td>
      <td>240</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3769</th>
      <td>Animals, Pets &amp; Humane</td>
      <td>86.363636</td>
      <td>7.0</td>
      <td>U.S. Dollar</td>
      <td>173</td>
      <td>13000</td>
      <td>950</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
<p>1357 rows × 8 columns</p>
</div>




```python
group = munging.groupby('category')
frequency  = group.size().sort_values()
```


```python
#create graph showing frequency of categories on fundrazer.com in the U.S
plt.figure(figsize = (12,10))
frequency.plot.bar(color = 'purple')
plt.xlabel('category')
plt.ylabel('count')
plt.title('Frequency of categories')
```




    Text(0.5,1,'Frequency of categories')




![png](output_20_1.png)



```python
#create a bar graph to find the average number of contributors per group 
plt.figure(figsize = (12,12))
munging.groupby('category')['numbercontributors'].mean().sort_values().plot.bar(color = 'g')
plt.ylabel('average contributors')
plt.title('average contributors per category')
```




    Text(0.5,1,'average contributors per category')




![png](output_21_1.png)



```python
#create a horizontal bar plot to show the average amount raised per category
plt.figure(figsize=(12,12))
munging.groupby('category')['amountraised'].mean().sort_values().plot.barh(color = 'b')
plt.ylabel('category')
plt.xlabel('amount raised')
plt.title('Average Amount raised per Category')
```




    Text(0.5,1,'Average Amount raised per Category')




![png](output_22_1.png)



```python
#create a bar graph to portray the average contribution given by person to each category
plt.figure(figsize = (12,6))
data.groupby('category')['averagecontribution'].mean().sort_values().plot.bar(color = 'r')
plt.ylabel('average contribution')

plt.title('Average number donation per person')
```




    Text(0.5,1,'Average number donation per person')




![png](output_23_1.png)



```python
#horizontal bar graph to show how many days on average a campaign is open per category
plt.figure(figsize = (12,12))
data.groupby('category')['days'].mean().sort_values().plot.barh(color = 'y')
plt.ylabel('category')
plt.xlabel('days')
plt.title('average days open')
```




    Text(0.5,1,'average days open')




![png](output_24_1.png)



```python
#category showing how much of a target amount each campaign has set up per category
plt.figure(figsize = (12,12))
data.groupby('category')['target'].median().sort_values().plot.barh(color = 'g')
plt.ylabel('category')
plt.xlabel('target')
plt.title('Target Set')
```




    Text(0.5,1,'Target Set')




![png](output_25_1.png)



```python
#Bar chart depicting percent completed 
plt.figure(figsize = (12,12))
data.groupby('category')['percent_complt'].median().sort_values().plot.bar(color = 'y')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1eab16e3160>




![png](output_26_1.png)



```python
#heat map depicting correlation between factors
import seaborn as sns
Var_Corr = data.corr()
# plot the heatmap and annotation on it
sns.heatmap(Var_Corr, xticklabels=Var_Corr.columns, yticklabels=Var_Corr.columns, annot=True)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1eab101bcc0>




![png](output_27_1.png)



```python
from wordcloud import WordCloud
wc = WordCloud(background_color="white", max_words=2000)
# generate word cloud
wc.generate(' '.join(munging['title']))
```




    <wordcloud.wordcloud.WordCloud at 0x1eab19b75c0>




```python
#shows most popular words used in titles
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure(figsize=(4, 3))
plt.axis("off")
plt.show()
```


![png](output_29_0.png)



![png](output_29_1.png)



```python

```
