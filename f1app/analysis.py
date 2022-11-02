import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64
import numpy as np
import pandas as pd
import seaborn as sb


class ChartGenerator():
        """
        @staticmethod
        def first_ten():
                fig, ax = plt.subplots()
                ax.plot([1, 3, 4], [3, 2, 5])
                #return fig

                flike = io.BytesIO()
                fig.savefig(flike)
                b64 = base64.b64encode(flike.getvalue()).decode()
                print(b64)
                context = {}
                context['chart'] = b64
                return context
                """

        @staticmethod
        def first_ten():
        
                circuits = pd.read_csv(r"E:\f1project\f1app\data\circuits.csv",sep = ';', encoding='latin-1')
                constructor_results = pd.read_csv(r"E:\f1project\f1app\data\constructor_results.csv",sep = ',',encoding='utf-8')
                constructor_standings = pd.read_csv(r"E:\f1project\f1app\data\constructor_standings.csv",sep = ',',encoding='utf-8')
                constructors = pd.read_csv(r"E:\f1project\f1app\data\constructors.csv",sep = ',',encoding='utf-8')
                driver_standings = pd.read_csv(r"E:\f1project\f1app\data\driver_standings.csv",sep = ',',encoding='utf-8')
                drivers = pd.read_csv(r"E:\f1project\f1app\data\drivers.csv",sep = ';',encoding='utf-8')
                lap_times = pd.read_csv(r"E:\f1project\f1app\data\lap_times.csv",sep = ',',encoding='utf-8')
                pit_stops = pd.read_csv(r"E:\f1project\f1app\data\pit_stops.csv",sep = ',',encoding='utf-8')
                qualifying = pd.read_csv(r"E:\f1project\f1app\data\qualifying.csv",sep = ',',encoding='utf-8')
                races = pd.read_csv(r"E:\f1project\f1app\data\races.csv",sep = ';',encoding='utf-8')
                results = pd.read_csv(r"E:\f1project\f1app\data\results.csv",sep = ';', encoding='latin-1')
                seasons = pd.read_csv(r"E:\f1project\f1app\data\seasons.csv",sep = ',',encoding='utf-8')
                status = pd.read_csv(r"E:\f1project\f1app\data\status.csv",sep = ',',encoding='utf-8')

                #merge datasets
                df = pd.merge(results, races[["raceId", "year", "name", "round"]], on="raceId", how="left")
                df = pd.merge(df, drivers[["driverId", "driverRef", "nationality"]], on = "driverId", how="left")
                df = pd.merge(df, constructors[["constructorId", "name", "nationality"]], on="constructorId", how="left")

                #drop, rename, rearrange coloumns
                df.drop(["number", "position", "positionText", "laps", "fastestLap", "statusId", "resultId", "raceId", "driverId", "constructorId"], axis=1, inplace = True)
                df.rename(columns={"rank":"fastestLapRank", "name_x":"gpName", "nationality_x":"driverNationality", "name_y":"constructorName", "nationality_y":"constructorNationality", "driverRef":"driver"}, inplace = True)
                df = df[["year", "gpName", "round", "driver", "constructorName", "grid", "positionOrder", "points", "time", "milliseconds", "fastestLapRank", "fastestLapTime", "fastestLapSpeed", "driverNationality", "constructorNationality"]]

                #drop incomplete seasons
                df = df[df["year"]!=2021]
                df = df[df["year"]!=2022]

                #sort values
                df = df.sort_values(by=["year", "round", "positionOrder"], ascending = [False, True, True])

                #replace \N values
                df.time.replace("\\N", np.nan, inplace = True)
                df.milliseconds.replace("\\N", np.nan, inplace = True)
                df.fastestLapRank.replace("\\N", np.nan, inplace = True)
                df.fastestLapTime.replace("\\N", np.nan, inplace = True)
                df.fastestLapSpeed.replace("\\N", np.nan, inplace = True)

                #change datatypes
                df.fastestLapSpeed = df.fastestLapSpeed.astype(float)
                df.fastestLapRank = df.fastestLapRank.astype(float)
                df.milliseconds = df.milliseconds.astype(float)

                #reset index
                df.reset_index(drop=True, inplace = True)

                sb.set_palette("Set3")
                plt.rcParams["figure.figsize"]=10,6

                driver_winner = df.loc[df["positionOrder"]==1].groupby("driver")["positionOrder"].count().sort_values(ascending=False).to_frame().reset_index()

                sb.barplot(data=driver_winner, y ="positionOrder", x="driver", color="green", alpha=0.8)

                top10Drivers = driver_winner.head(10)
        
                fig = sb.barplot(data = top10Drivers, y = "positionOrder", x="driver", color="#636efa", alpha = 0.8, linewidth=.8, edgecolor="black").figure
                plt.title("Top 10 Gp Winners")
                plt.xlabel("Drivers")
                plt.ylabel("Number of Wins")

                flike = io.BytesIO()
                fig.savefig(flike)
                b64 = base64.b64encode(flike.getvalue()).decode()
                #context = {}
                #context['chart'] = b64

                return b64