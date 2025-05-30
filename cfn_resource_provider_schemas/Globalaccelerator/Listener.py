SCHEMA = {
  "typeName" : "AWS::GlobalAccelerator::Listener",
  "description" : "Resource Type definition for AWS::GlobalAccelerator::Listener",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-globalaccelerator",
  "definitions" : {
    "Port" : {
      "description" : "A network port number",
      "type" : "integer",
      "minimum" : 0,
      "maximum" : 65535
    },
    "PortRange" : {
      "description" : "A port range to support for connections from  clients to your accelerator.",
      "type" : "object",
      "properties" : {
        "FromPort" : {
          "$ref" : "#/definitions/Port"
        },
        "ToPort" : {
          "$ref" : "#/definitions/Port"
        }
      },
      "required" : [ "FromPort", "ToPort" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ListenerArn" : {
      "description" : "The Amazon Resource Name (ARN) of the listener.",
      "type" : "string"
    },
    "AcceleratorArn" : {
      "description" : "The Amazon Resource Name (ARN) of the accelerator.",
      "type" : "string"
    },
    "PortRanges" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/PortRange"
      }
    },
    "Protocol" : {
      "description" : "The protocol for the listener.",
      "type" : "string",
      "default" : "TCP",
      "enum" : [ "TCP", "UDP" ]
    },
    "ClientAffinity" : {
      "description" : "Client affinity lets you direct all requests from a user to the same endpoint.",
      "type" : "string",
      "default" : "NONE",
      "enum" : [ "NONE", "SOURCE_IP" ]
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "AcceleratorArn", "PortRanges", "Protocol" ],
  "createOnlyProperties" : [ "/properties/AcceleratorArn" ],
  "readOnlyProperties" : [ "/properties/ListenerArn" ],
  "primaryIdentifier" : [ "/properties/ListenerArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "globalaccelerator:CreateListener", "globalaccelerator:DescribeListener", "globalaccelerator:DescribeAccelerator" ]
    },
    "read" : {
      "permissions" : [ "globalaccelerator:DescribeListener" ]
    },
    "update" : {
      "permissions" : [ "globalaccelerator:UpdateListener", "globalaccelerator:DescribeListener", "globalaccelerator:DescribeAccelerator" ]
    },
    "delete" : {
      "permissions" : [ "globalaccelerator:DescribeListener", "globalaccelerator:DeleteListener", "globalaccelerator:DescribeAccelerator" ]
    },
    "list" : {
      "permissions" : [ "globalaccelerator:ListListeners" ]
    }
  },
  "additionalProperties" : False
}