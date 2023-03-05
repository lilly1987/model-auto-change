import modules.scripts as scripts
import gradio as gr
import os
import random

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state

v_cnt=getattr(opts, f"model-auto-change-cnt", 0)

def chg(enabled):
    if not enabled:
        logger.debug(f"{self.title()} disabled - exiting")
        return p
        
    lst=sd_models.checkpoints_list.values()
    print(f" opts.sd_model_checkpoint : { lst }")
    #opts.sd_model_checkpoint 
    print(f" opts.sd_model_checkpoint : { opts.sd_model_checkpoint }")
    #sd_models.reload_model_weights()
    print(f" cnt : { v_cnt }")
    
    return p

class Script(scripts.Script):  
    
    #def __init__(self):
    #    print(f"{self.title()} __init__")
        
    # The title of the script. This is what will be displayed in the dropdown menu.
    def title(self):
        #print(f"model-auto-change")
        return "model-auto-change"


    # Determines when the script should be shown in the dropdown menu via the 
    # returned value. As an example:
    # is_img2img is True if the current tab is img2img, and False if it is txt2img.
    # Thus, return is_img2img to only show the script on the img2img tab.

    def show(self, is_img2img):
        print(f"{self.title()} show {is_img2img}")
        return scripts.AlwaysVisible

# How the script's is displayed in the UI. See https://gradio.app/docs/#components
# for the different UI components you can use and how to create them.
# Most UI components can return a value, such as a boolean for a checkbox.
# The returned values are passed to the run method as parameters.

    def ui(self, is_img2img):
        print(f"{self.title()} ui {is_img2img}")
        enabled = gr.Checkbox(value=False, label="random apply")
        with gr.Group():
            with gr.Accordion(self.title(), open=False):
                enabled = gr.Checkbox(value=False, label="random apply")
        return [enabled]



# This is where the additional processing is implemented. The parameters include
# self, the model object "p" (a StableDiffusionProcessing class, see
# processing.py), and the parameters returned by the ui method.
# Custom functions can be defined here, and additional libraries can be imported 
# to be used in processing. The return value should be a Processed object, which is
# what is returned by the process_images method.
    def process(self, p
        , enabled
    ):  #noHypernetwork,rHypernetworks,sd_hypernetwork_strength1,sd_hypernetwork_strength2,
        print(f"{self.title()} process")
        #chg(enabled)
        return 
        
        
    #def process_batch(self, p
    #    , enabled
    #    , batch_number, prompts, seeds, subseeds
    #):  #noHypernetwork,rHypernetworks,sd_hypernetwork_strength1,sd_hypernetwork_strength2,
    #    print(f"{self.title()} process_batch")
    #    chg(enabled)
    #    return 
        
        
    #def run(self, p, enabled):
    #    
    #    return chg(enabled)
    
    #def postprocess(self, *args):
    #    return