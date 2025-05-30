SCHEMA = {
  "typeName" : "AWS::GroundStation::DataflowEndpointGroup",
  "description" : "AWS Ground Station DataflowEndpointGroup schema for CloudFormation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ground-station.git",
  "definitions" : {
    "SocketAddress" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string"
        },
        "Port" : {
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    },
    "AgentStatus" : {
      "description" : "The status of AgentEndpoint.",
      "type" : "string",
      "enum" : [ "SUCCESS", "FAILED", "ACTIVE", "INACTIVE" ]
    },
    "AuditResults" : {
      "description" : "The results of the audit.",
      "type" : "string",
      "enum" : [ "HEALTHY", "UNHEALTHY" ]
    },
    "IntegerRange" : {
      "description" : "An integer range that has a minimum and maximum value.",
      "type" : "object",
      "properties" : {
        "Minimum" : {
          "description" : "A minimum value.",
          "type" : "integer"
        },
        "Maximum" : {
          "description" : "A maximum value.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    },
    "RangedSocketAddress" : {
      "description" : "A socket address with a port range.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "description" : "IPv4 socket address.",
          "type" : "string"
        },
        "PortRange" : {
          "description" : "Port range of a socket address.",
          "$ref" : "#/definitions/IntegerRange"
        }
      },
      "additionalProperties" : False
    },
    "ConnectionDetails" : {
      "description" : "Egress address of AgentEndpoint with an optional mtu.",
      "type" : "object",
      "properties" : {
        "SocketAddress" : {
          "$ref" : "#/definitions/SocketAddress"
        },
        "Mtu" : {
          "description" : "Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    },
    "RangedConnectionDetails" : {
      "description" : "Ingress address of AgentEndpoint with a port range and an optional mtu.",
      "type" : "object",
      "properties" : {
        "SocketAddress" : {
          "$ref" : "#/definitions/RangedSocketAddress"
        },
        "Mtu" : {
          "description" : "Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    },
    "AwsGroundStationAgentEndpoint" : {
      "description" : "Information about AwsGroundStationAgentEndpoint.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : "^[ a-zA-Z0-9_:-]{1,256}$"
        },
        "EgressAddress" : {
          "$ref" : "#/definitions/ConnectionDetails"
        },
        "IngressAddress" : {
          "$ref" : "#/definitions/RangedConnectionDetails"
        },
        "AgentStatus" : {
          "$ref" : "#/definitions/AgentStatus"
        },
        "AuditResults" : {
          "$ref" : "#/definitions/AuditResults"
        }
      },
      "additionalProperties" : False
    },
    "DataflowEndpoint" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : "^[ a-zA-Z0-9_:-]{1,256}$"
        },
        "Address" : {
          "$ref" : "#/definitions/SocketAddress"
        },
        "Mtu" : {
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    },
    "SecurityDetails" : {
      "type" : "object",
      "properties" : {
        "SubnetIds" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "SecurityGroupIds" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "RoleArn" : {
          "type" : "string",
          "pattern" : "^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$"
        }
      },
      "additionalProperties" : False
    },
    "EndpointDetails" : {
      "type" : "object",
      "properties" : {
        "SecurityDetails" : {
          "$ref" : "#/definitions/SecurityDetails"
        },
        "Endpoint" : {
          "$ref" : "#/definitions/DataflowEndpoint"
        },
        "AwsGroundStationAgentEndpoint" : {
          "$ref" : "#/definitions/AwsGroundStationAgentEndpoint"
        }
      },
      "oneOf" : [ {
        "required" : [ "Endpoint", "SecurityDetails" ]
      }, {
        "required" : [ "AwsGroundStationAgentEndpoint" ]
      } ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^[ a-zA-Z0-9\\+\\-=._:/@]{1,128}$"
        },
        "Value" : {
          "type" : "string",
          "pattern" : "^[ a-zA-Z0-9\\+\\-=._:/@]{1,256}$"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$"
    },
    "EndpointDetails" : {
      "type" : "array",
      "minItems" : 1,
      "items" : {
        "$ref" : "#/definitions/EndpointDetails"
      }
    },
    "ContactPrePassDurationSeconds" : {
      "type" : "integer",
      "description" : "Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state."
    },
    "ContactPostPassDurationSeconds" : {
      "type" : "integer",
      "description" : "Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state."
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "EndpointDetails" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/EndpointDetails", "/properties/ContactPrePassDurationSeconds", "/properties/ContactPostPassDurationSeconds" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "groundstation:TagResource", "groundstation:UntagResource", "groundstation:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "groundstation:CreateDataflowEndpointGroup", "groundstation:GetDataflowEndpointGroup", "groundstation:TagResource", "iam:PassRole", "ec2:describeAddresses", "ec2:describeNetworkInterfaces", "iam:createServiceLinkedRole" ]
    },
    "update" : {
      "permissions" : [ "groundstation:ListTagsForResource", "groundstation:TagResource", "groundstation:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "groundstation:GetDataflowEndpointGroup", "groundstation:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "groundstation:DeleteDataflowEndpointGroup", "groundstation:GetDataflowEndpointGroup" ]
    },
    "list" : {
      "permissions" : [ "groundstation:ListDataflowEndpointGroups" ]
    }
  },
  "additionalProperties" : False
}