SCHEMA = {
  "typeName" : "AWS::EC2::NetworkInsightsPath",
  "description" : "Resource schema for AWS::EC2::NetworkInsightsPath",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2-ni.git",
  "definitions" : {
    "Tags" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Key" ]
    },
    "IpAddress" : {
      "type" : "string"
    },
    "Protocol" : {
      "type" : "string",
      "enum" : [ "tcp", "udp" ]
    },
    "Port" : {
      "type" : "integer"
    },
    "FilterPortRange" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FromPort" : {
          "type" : "integer"
        },
        "ToPort" : {
          "type" : "integer"
        }
      }
    },
    "PathFilter" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SourceAddress" : {
          "$ref" : "#/definitions/IpAddress"
        },
        "SourcePortRange" : {
          "$ref" : "#/definitions/FilterPortRange"
        },
        "DestinationAddress" : {
          "$ref" : "#/definitions/IpAddress"
        },
        "DestinationPortRange" : {
          "$ref" : "#/definitions/FilterPortRange"
        }
      }
    }
  },
  "properties" : {
    "NetworkInsightsPathId" : {
      "type" : "string"
    },
    "NetworkInsightsPathArn" : {
      "type" : "string"
    },
    "CreatedDate" : {
      "type" : "string"
    },
    "SourceIp" : {
      "$ref" : "#/definitions/IpAddress"
    },
    "FilterAtSource" : {
      "$ref" : "#/definitions/PathFilter"
    },
    "FilterAtDestination" : {
      "$ref" : "#/definitions/PathFilter"
    },
    "DestinationIp" : {
      "$ref" : "#/definitions/IpAddress"
    },
    "Source" : {
      "type" : "string"
    },
    "Destination" : {
      "type" : "string"
    },
    "SourceArn" : {
      "type" : "string"
    },
    "DestinationArn" : {
      "type" : "string"
    },
    "Protocol" : {
      "$ref" : "#/definitions/Protocol"
    },
    "DestinationPort" : {
      "$ref" : "#/definitions/Port"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags" ]
  },
  "required" : [ "Protocol", "Source" ],
  "readOnlyProperties" : [ "/properties/NetworkInsightsPathId", "/properties/NetworkInsightsPathArn", "/properties/CreatedDate", "/properties/SourceArn", "/properties/DestinationArn" ],
  "primaryIdentifier" : [ "/properties/NetworkInsightsPathId" ],
  "createOnlyProperties" : [ "/properties/SourceIp", "/properties/DestinationIp", "/properties/Source", "/properties/Destination", "/properties/Protocol", "/properties/DestinationPort", "/properties/FilterAtSource", "/properties/FilterAtDestination" ],
  "additionalIdentifiers" : [ [ "/properties/NetworkInsightsPathArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateNetworkInsightsPath", "ec2:CreateTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteNetworkInsightsPath", "ec2:DeleteTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeNetworkInsightsPaths" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeNetworkInsightsPaths" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeNetworkInsightsPaths", "ec2:CreateTags", "ec2:DeleteTags" ]
    }
  }
}