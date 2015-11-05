//
'use strict';

/**
 * @ngdoc function
 * @name introspectorApp.controller:GraphCtrl
 * @description
 * # TreeCtrl
 * Controller of the introspectorApp
 */

angular.module(
    'introspectorApp')
    .controller(
        'GraphCtrl',
        [
            '$scope',
            function ($scope) {
                
                
                var width = 960,
                    height = 500;

                var color = d3.scale.category20();

                var force = d3.layout.force()
                    .charge(-120)
                    .linkDistance(30)
                    .size([width, height]);

                var svg = d3.select("#d3graph")
                    .attr("width", width)
                    .attr("height", height);

                var nodes = [];
                var links = [];

                var raw_data_object={};
                eval($("#raw-data-object").data("ngInit"));
                var data=raw_data_object;
                
                var nodecount = 0;

                function visit_node(node){
                    nodecount = nodes.length;
                    var gnode =  {
                        name : "Node" + nodecount,
                        source: JSON.stringify(node),
                        weight :  1,
                        group : 1,
                    };
                    nodes.push(gnode);
                    return nodecount
                }

                function add_link(from, to, weight) {
                    var l = {
                        type : 'number',
                        source: from,
                        target : to,
                        value : weight
                    };
                    links.push(l);
                    return l;
                }

                function visit_array(node) {
                    array_object = visit_node("Array");
                    
                    for (var i = 0; i < node.length; ++i) {
                        var child = visit_tree(path, node[i], func);
                        add_link(array_object, child, 10);
                    }
                    
                    return array_object;
                }

                function visit_tree(node) {

                    var gnode = visit_node(node);
                    var o=nodes[gnode];
                    
                    if (node == null) {
                        return 0;
                    }
                    
                    var typename = typeof node;
                    
                    switch (typename) {
                    case 'string':
                        o['val']=node;
                        return gnode;
                        break;
                    case 'number':
                        o['val']=node;
                        return gnode;
                        break;

                    case 'object':

                        var keys = Object.keys(node);
                        for (var key of keys) {
                            var child = visit_tree(node[key]);
                            var l = add_link(gnode, child, 20);
                            l['name']=(key)
                        }
                        return gnode;
                        break;
                        
                    default :
                        console.log(typename)    
                    }
                
                    if (node instanceof Array) {
                        
                        gnode = visit_array(node);
                        return gnode;
                    }
                    else {
                        console.log(typename);
                        console.log(node);
                    }
                }

                visit_tree(data);
                console.log(nodes);
                console.log(links);
                force
                    .nodes(nodes)
                    .links(links)
                    .start();

                var link = svg.selectAll(".link")
                    .data(links)
                    .enter().append("line")
                    .attr("class", "link")
                    .style("stroke-width", function(d) { return Math.sqrt(d.value); });

                var node = svg.selectAll(".node")
                    .data(nodes)
                    .enter().append("circle")
                    .attr("class", "node")
                    .attr("r", 5)
                    .style("fill", function(d) { return color(d.group); })
                    .call(force.drag);

                node.append("title")
                    .text(function(d) { return d.name; });

                force.on("tick", function() {
                    link.attr("x1", function(d) { return d.source.x; })
                        .attr("y1", function(d) { return d.source.y; })
                        .attr("x2", function(d) { return d.target.x; })
                        .attr("y2", function(d) { return d.target.y; });
                    
                    node.attr("cx", function(d) { return d.x; })
                        .attr("cy", function(d) { return d.y; });
                });
                               
            }]);

