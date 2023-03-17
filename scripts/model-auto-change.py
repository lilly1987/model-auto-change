import modules.scripts as scripts
import gradio as gr
import os
import random

from modules import images, sd_models
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state



class Script(scripts.Script):  
    
    v_max=getattr(opts, f"model-auto-change-max", 10)
    v_cnt=getattr(opts, f"model-auto-change-cnt", 1)
    v_model=None
    
    def maxSet(self):
        self.v_cnt=self.v_max
            
    def nextSet(self):

        lst=list(sd_models.checkpoints_list.keys())
        print(f" opts.sd_model_checkpoint : { lst }")        
        opts.sd_model_checkpoint = random.choice(lst)
        print(f" opts.sd_model_checkpoint : { opts.sd_model_checkpoint }")
        sd_models.reload_model_weights()
        self.v_cnt=1
        print(f" cnt : { self.v_cnt }")
        
    def chg(self, enabled):
        self.v_model=opts.sd_model_checkpoint 
        if not enabled:
            print(f"{self.title()} disabled - exiting")
            return
            
        #global v_cnt
        print(f" cnt : { self.v_cnt } / { self.v_max }")
        if self.v_cnt<self.v_max:
            self.v_cnt+=1
            return

        self.nextSet()
        
        return
    
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
        enabled = gr.Checkbox(value=False, label="model random apply")
        accordion = gr.Group(visible=False)
        enabled.change(
            fn=lambda x: {"visible": x, "__type__": "update"},
            inputs=[enabled],
            outputs=[accordion],
            show_progress = False)
        with accordion:
            max = gr.Slider(minimum=1,maximum=100,step=1,label='count max',value=10)
            max_btn = gr.Button("count max set")
            max_btn.click(fn=self.maxSet)
            next_btn = gr.Button("next model")
            next_btn.click(fn=self.nextSet)
        #with gr.Group():
        #    with gr.Accordion(self.title(), open=False):
        #        enabled = gr.Checkbox(value=False, label="model random apply")
        return [enabled,max]



# This is where the additional processing is implemented. The parameters include
# self, the model object "p" (a StableDiffusionProcessing class, see
# processing.py), and the parameters returned by the ui method.
# Custom functions can be defined here, and additional libraries can be imported 
# to be used in processing. The return value should be a Processed object, which is
# what is returned by the process_images method.
    def process(self, p
        , enabled
        , max
    ):  #noHypernetwork,rHypernetworks,sd_hypernetwork_strength1,sd_hypernetwork_strength2,
        print(f"{self.title()} process")
        
        self.v_max=max
        self.chg(enabled)
        return 
        
        
    #def process_batch(self, p
    #    , enabled
    #    , batch_number, prompts, seeds, subseeds
    #):  #noHypernetwork,rHypernetworks,sd_hypernetwork_strength1,sd_hypernetwork_strength2,
    #    print(f"{self.title()} process_batch")
    #    #chg(enabled)
    #    return 
        
        
    #def run(self, p, enabled):
    #    
    #    return chg(enabled)
    
    def postprocess(self, *args):
        print(f"{self.title()} postprocess")
        #opts.sd_model_checkpoint = self.v_model
        return