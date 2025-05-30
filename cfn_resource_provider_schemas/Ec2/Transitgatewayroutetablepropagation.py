SCHEMA = {
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-transitgateway/aws-ec2-transitgatewayroutetablepropagation",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "ec2:GetTransitGatewayRouteTablePropagations" ]
    },
    "create" : {
      "permissions" : [ "ec2:GetTransitGatewayRouteTablePropagations", "ec2:EnableTransitGatewayRouteTablePropagation" ]
    },
    "list" : {
      "permissions" : [ "ec2:GetTransitGatewayRouteTablePropagations" ],
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
      "permissions" : [ "ec2:GetTransitGatewayRouteTablePropagations", "ec2:DisableTransitGatewayRouteTablePropagation" ]
    }
  },
  "typeName" : "AWS::EC2::TransitGatewayRouteTablePropagation",
  "description" : "AWS::EC2::TransitGatewayRouteTablePropagation Type",
  "createOnlyProperties" : [ "/properties/TransitGatewayAttachmentId", "/properties/TransitGatewayRouteTableId" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/TransitGatewayRouteTableId", "/properties/TransitGatewayAttachmentId" ],
  "definitions" : { },
  "required" : [ "TransitGatewayRouteTableId", "TransitGatewayAttachmentId" ],
  "properties" : {
    "TransitGatewayRouteTableId" : {
      "description" : "The ID of transit gateway route table.",
      "type" : "string"
    },
    "TransitGatewayAttachmentId" : {
      "description" : "The ID of transit gateway attachment.",
      "type" : "string"
    }
  }
}