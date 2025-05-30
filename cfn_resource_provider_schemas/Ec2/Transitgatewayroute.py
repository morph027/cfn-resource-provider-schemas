SCHEMA = {
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "typeName" : "AWS::EC2::TransitGatewayRoute",
  "description" : "Resource Type definition for AWS::EC2::TransitGatewayRoute",
  "createOnlyProperties" : [ "/properties/TransitGatewayRouteTableId", "/properties/TransitGatewayAttachmentId", "/properties/DestinationCidrBlock", "/properties/Blackhole" ],
  "primaryIdentifier" : [ "/properties/TransitGatewayRouteTableId", "/properties/DestinationCidrBlock" ],
  "required" : [ "TransitGatewayRouteTableId", "DestinationCidrBlock" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-transitgateway.git",
  "handlers" : {
    "read" : {
      "permissions" : [ "ec2:SearchTransitGatewayRoutes" ]
    },
    "create" : {
      "permissions" : [ "ec2:CreateTransitGatewayRoute", "ec2:SearchTransitGatewayRoutes" ]
    },
    "list" : {
      "permissions" : [ "ec2:SearchTransitGatewayRoutes" ],
      "handlerSchema" : {
        "properties" : {
          "TransitGatewayRouteTableId" : {
            "$ref" : "resource-schema.json#/properties/TransitGatewayRouteTableId"
          }
        },
        "required" : [ "TransitGatewayRouteTableId" ]
      }
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteTransitGatewayRoute", "ec2:SearchTransitGatewayRoutes" ]
    }
  },
  "additionalProperties" : False,
  "definitions" : { },
  "properties" : {
    "TransitGatewayRouteTableId" : {
      "description" : "The ID of transit gateway route table.",
      "type" : "string"
    },
    "DestinationCidrBlock" : {
      "description" : "The CIDR range used for destination matches. Routing decisions are based on the most specific match.",
      "type" : "string"
    },
    "Blackhole" : {
      "description" : "Indicates whether to drop traffic that matches this route.",
      "type" : "boolean"
    },
    "TransitGatewayAttachmentId" : {
      "description" : "The ID of transit gateway attachment.",
      "type" : "string"
    }
  },
  "replacementStrategy" : "delete_then_create"
}