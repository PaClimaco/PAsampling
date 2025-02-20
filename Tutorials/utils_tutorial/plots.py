import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()

def format_fn(value, tick_number):
    return f"{value/1000:.0f}K"
def generate_lineplots(dataset, df, given_strategies = None, filepath = None):

        df = df[df['strategy'].isin(given_strategies)]
        custom_x_values = ['5%', '10%', '20%', '25%']
        x_values = list(set(list(df["num_selected"])))
        x_values.sort()
        # Change unit of measure of label value, from kcal/mol to eV for plot consistency with other datasets
        if dataset == 'QM7':
                df[['RMSE', 'MAE', 'MAXAE']] = df[['RMSE', 'MAE',  'MAXAE']]/23.060900 #from kcal/mol to ev

        colors = {
        'FPS': "royalblue",
        'RDM': "limegreen",
        'FacilityLocation':"orange",
        'k-medoids++': "violet",
        'FPS-RDM': "limegreen",
        'FPS-FacLoc': "orange",  
        'FPS-k-medoids++': "violet", 
        'DAFPS': 'red',
        'Twinning': 'black',

        }
        
        dashes_dict = {
        'FPS': '',
        'RDM': '',
        'FacilityLocation': '',
        'k-medoids++': '',
        'FPS-RDM': (5, 2),
        'FPS-FacLoc': (5, 2),  
        'FPS-k-medoids++': (5, 2),  
        'DA-FPS_torch': '',
        'DAFPS': '',
        'Twinning': '',
      
        }    
        for metric in ['MAE', 'RMSE',  'MAXAE']:
                plt.figure(figsize=(10,7))
                sns.lineplot(data=df, 
                        x="num_selected",
                        y=metric,
                        hue="strategy",
                        style="strategy",
                        dashes= dashes_dict,
                        errorbar = "se",
                        err_style = 'bars',
                        markers= False, 
                        hue_order= given_strategies,
                        legend=True,
                        palette=colors,
                        )
                plt.tick_params(labelsize=18)
                plt.legend(loc='upper right', prop={'size': 13}, bbox_to_anchor=(1.008, 1))
                plt.ylabel(f"{metric}", fontsize=20)
                plt.xlabel("Number of training samples", fontsize=20)
                plt.xticks(x_values, custom_x_values)
                sns.set_style("darkgrid")

                plt.show()
                
        return 
        


def generate_barplots(dataset, file, filepath = None):
    if isinstance(file, pd.DataFrame):
        df = file
    else:
        df = pd.read_csv(file)    
        filepath = file
 
    x_values = list(set(list(df["num_selected"])))
    x_values.sort()

    value_to_string = {x_values[0]: '1%', x_values[1]: '3%', x_values[2]: '5%',x_values[3]: '7%', x_values[4]: '10%'}
    
    # Apply the mapping to the "num_selected" column
    df['x_axis'] = df['num_selected'].map(value_to_string)
    
    # Change unit of measure of label value, from kcal/mol to eV for plot consistency with other datasets
    if dataset == 'QM7':
                df[['RMSE', 'MAE', 'MAXAE']] = df[['RMSE', 'MAE',  'MAXAE']]/23.060900 #from kcal/mol to ev
    
    for metric in ['MAXAE', 'MAE', 'RMSE']:
        g = sns.catplot(data=df, 
                    x="x_axis",
                    y=metric,
                    hue="strategy",
                    errorbar = "sd",
                    kind="bar",
                    capsize=0.05, 
                    height=5,
                    aspect=1.5,
                    hue_order= ["FPS","RDM","FacilityLocation", "k-medoids++"],
                    legend=False,
                    )
        g.fig.set_size_inches(10,7)
        plt.tick_params(labelsize =  20)
        plt.legend(loc='upper right',prop={'size': 15},  bbox_to_anchor=(1.008, 1))
        plt.ylabel(f"{metric} [eV]",fontsize=20)
        plt.xlabel("Amount of training samples", fontsize=20)
        plt.tight_layout()
        plt.show()
        if filepath:
            save_path = "_".join([filepath.strip(".csv"), metric]) + ".pdf"
            print(f"Save {save_path}")
            plt.savefig(save_path)
        
        plt.close()
        

def generate_lineplots_analysis(file, filepath=None):
    # Load data from file
    if isinstance(file, pd.DataFrame):
        df = file
    else:
        df = pd.read_csv(file)
        filepath = file
    # Define x-axis values and custom labels
    x_values = sorted(list(set(df["num_selected"])))
    custom_x_values = ['1%','3%','5%','7%', '10%']

    # Plot line plots for different metrics
    for metric in ['fill distance', 'regularized condition number', 'condition number']:
        plt.figure(figsize=(10, 7))
        g = sns.lineplot(data=df,
                        x="num_selected",
                        y=metric,
                        hue="strategy",
                        style="strategy",
                        dashes=False,
                        errorbar="sd",
                        err_style='band',
                        markers=["s", "D", "X", "o"],
                        hue_order=["FPS", "RDM", "FacilityLocation", "k-medoids++"],
                        legend=True,
                        )

        # Customize legends and plot properties
        if metric == 'fill distance':
            plt.legend(loc='upper right', prop={'size': 15}, bbox_to_anchor=(1.008, 1))

        if metric in ['regularized condition number', 'condition number']:
            plt.yscale('log')
            plt.legend(loc='lower right', prop={'size': 15})
            
        plt.xscale('log')
        plt.ylabel(f"{metric}", fontsize=20)
        plt.xlabel("Amount of training samples from QM7", fontsize=20)
        plt.xticks(x_values, custom_x_values)
        plt.tick_params(labelsize=18)
       

        # Save the plot if filepath is provided
        if filepath:
            save_path = "_".join([filepath.strip(".csv"), metric]) + ".pdf"
            print(f"Save {save_path}")
            plt.savefig(save_path)

        # Configure overall plot appearance and show the plot
        fig = plt.gcf()
        fig.set_clip_box([0, 0, 1, 1])
        plt.tight_layout()
        plt.show()
        plt.close()
