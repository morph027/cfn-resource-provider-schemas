SCHEMA = {
  "typeName" : "AWS::GlobalAccelerator::EndpointGroup",
  "description" : "Resource Type definition for AWS::GlobalAccelerator::EndpointGroup",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-globalaccelerator",
  "definitions" : {
    "EndpointConfiguration" : {
      "description" : "The configuration for a given endpoint",
      "type" : "object",
      "properties" : {
        "EndpointId" : {
          "description" : "Id of the endpoint. For Network/Application Load Balancer this value is the ARN.  For EIP, this value is the allocation ID.  For EC2 instances, this is the EC2 instance ID",
          "type" : "string"
        },
        "AttachmentArn" : {
          "description" : "Attachment ARN that provides access control to the cross account endpoint. Not required for resources hosted in the same account as the endpoint group.",
          "type" : "string"
        },
        "Weight" : {
          "description" : "The weight for the endpoint.",
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 255,
          "default" : 100
        },
        "ClientIPPreservationEnabled" : {
          "description" : "True if client ip should be preserved",
          "type" : "boolean",
          "default" : True
        }
      },
      "required" : [ "EndpointId" ],
      "additionalProperties" : False
    },
    "Port" : {
      "description" : "A network port number",
      "type" : "integer",
      "minimum" : 0,
      "maximum" : 65535
    },
    "PortOverride" : {
      "description" : "listener to endpoint port mapping.",
      "type" : "object",
      "properties" : {
        "ListenerPort" : {
          "$ref" : "#/definitions/Port"
        },
        "EndpointPort" : {
          "$ref" : "#/definitions/Port"
        }
      },
      "required" : [ "ListenerPort", "EndpointPort" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ListenerArn" : {
      "description" : "The Amazon Resource Name (ARN) of the listener",
      "type" : "string"
    },
    "EndpointGroupRegion" : {
      "description" : "The name of the AWS Region where the endpoint group is located",
      "type" : "string"
    },
    "EndpointConfigurations" : {
      "description" : "The list of endpoint objects.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/EndpointConfiguration"
      }
    },
    "TrafficDialPercentage" : {
      "description" : "The percentage of traffic to sent to an AWS Region",
      "type" : "number",
      "minimum" : 0,
      "maximum" : 100,
      "default" : 100
    },
    "HealthCheckPort" : {
      "description" : "The port that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.",
      "type" : "integer",
      "minimum" : -1,
      "maximum" : 65535,
      "default" : -1
    },
    "HealthCheckProtocol" : {
      "description" : "The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.",
      "type" : "string",
      "default" : "TCP",
      "enum" : [ "TCP", "HTTP", "HTTPS" ]
    },
    "HealthCheckPath" : {
      "description" : "",
      "type" : "string",
      "default" : "/"
    },
    "HealthCheckIntervalSeconds" : {
      "description" : "The time in seconds between each health check for an endpoint. Must be a value of 10 or 30",
      "type" : "integer",
      "default" : 30
    },
    "ThresholdCount" : {
      "description" : "The number of consecutive health checks required to set the state of the endpoint to unhealthy.",
      "type" : "integer",
      "default" : 3
    },
    "EndpointGroupArn" : {
      "description" : "The Amazon Resource Name (ARN) of the endpoint group",
      "type" : "string"
    },
    "PortOverrides" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/PortOverride"
      }
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "ListenerArn", "EndpointGroupRegion" ],
  "createOnlyProperties" : [ "/properties/EndpointGroupRegion", "/properties/ListenerArn" ],
  "writeOnlyProperties" : [ "/properties/EndpointConfigurations/*/AttachmentArn" ],
  "readOnlyProperties" : [ "/properties/EndpointGroupArn" ],
  "primaryIdentifier" : [ "/properties/EndpointGroupArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "globalaccelerator:CreateEndpointGroup", "globalaccelerator:DescribeEndpointGroup", "globalaccelerator:DescribeAccelerator", "globalaccelerator:DescribeListener", "globalaccelerator:ListAccelerators", "globalaccelerator:ListListeners" ]
    },
    "read" : {
      "permissions" : [ "globalaccelerator:DescribeEndpointGroup" ]
    },
    "update" : {
      "permissions" : [ "globalaccelerator:UpdateEndpointGroup", "globalaccelerator:DescribeEndpointGroup", "globalaccelerator:DescribeListener", "globalaccelerator:DescribeAccelerator" ]
    },
    "delete" : {
      "permissions" : [ "globalaccelerator:DeleteEndpointGroup", "globalaccelerator:DescribeEndpointGroup", "globalaccelerator:DescribeAccelerator" ]
    },
    "list" : {
      "permissions" : [ "globalaccelerator:ListEndpointGroups" ]
    }
  },
  "additionalProperties" : False
}