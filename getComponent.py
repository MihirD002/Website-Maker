def get_component_code(component_type, position):

    components = {
        "Accordion Default": accordion_def_template,
        "Accordion Expanded": accordion_expanded_template
    }

    template = components.get(component_type)

    positioned_component = template.format(
        component_class=f"{component_type.lower()}-component",
        left=position['left'],
        top=position['top'],
        width=position['width'],
        height=position['height']
    )

    return positioned_component


accordion_def_template = """
<div class="accordion" id="accordionExample">
<div class="{component_class}" style="position: absolute; left: {left}; top: {top}; width: {width}; height: {height};">
<div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse" aria-expanded="false" aria-controls="collapse">
        Accordion Item 
      </button>
    </h2>
    <div id="collapse" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
      </div>
    </div>
  </div>
</div>
</div>
"""

accordion_expanded_template = """
<div class="accordion" id="accordionExample">
<div class="{component_class}" style="position: absolute; left: {left}; top: {top}; width: {width}; height: {height};">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse" aria-expanded="true" aria-controls="collapse">
        Accordion 
      </button>
    </h2>
    <div id="collapse" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
      </div>
    </div>
  </div>
  </div>
</div>
"""
