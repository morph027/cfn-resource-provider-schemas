SCHEMA = {
  "typeName" : "AWS::EC2::TrafficMirrorTarget",
  "description" : "Resource Type definition for AWS::EC2::TrafficMirrorTarget",
  "additionalProperties" : False,
  "properties" : {
    "NetworkLoadBalancerArn" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "NetworkInterfaceId" : {
      "type" : "string"
    },
    "GatewayLoadBalancerEndpointId" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "createOnlyProperties" : [ "/properties/GatewayLoadBalancerEndpointId", "/properties/NetworkLoadBalancerArn", "/properties/NetworkInterfaceId", "/properties/Description" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}