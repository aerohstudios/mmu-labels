module GenerateLabel(
    title="",
    subtitle="",
    font="evogria",
    textOnly=false,
    backgroundOnly=false,
    coreOnly=false,
    ) {
    $fn=128;
    
    if (!textOnly && backgroundOnly) {
        translate([0, 0, 2.1]) {
            color("black")
            minkowski() {
                cube([47-4,14.5-4,.1], true);
                // rounded corners
                cylinder(r=2,h=2.9-2.1);
            }
        }
    }
    
    if (!textOnly && coreOnly) {
        color("white")
        minkowski() {
            cube([47-4,14.5-4,.1], true);
            // rounded corners
            cylinder(r=2,h=2.9-0.9);
        }
    }

    if (!backgroundOnly) {
        if (title != "") {
            if (subtitle == "") {
                translate([0,-3.5,2]) {
                    color("white") linear_extrude(1) 
                    text(title, size=7, font=font, halign="center");
                } 
            } else {
                translate([0,-0.5,2]) {
                    color("white") linear_extrude(1) 
                    text(title, size=5, font=font, halign="center");
                }
            }
        }

        if (subtitle != "") {
            translate([0,-5.5,2]) {
                color("white") linear_extrude(1) 
                text(subtitle, size=3, font=font, halign="center");
            }
        }
    }
};
