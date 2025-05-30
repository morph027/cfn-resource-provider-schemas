SCHEMA = {
  "typeName" : "AWS::EC2::VPNGatewayRoutePropagation",
  "description" : "Resource Type definition for AWS::EC2::VPNGatewayRoutePropagation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "RouteTableIds" : {
      "description" : "The ID of the route table. The routing table must be associated with the same VPC that the virtual private gateway is attached to",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "VpnGatewayId" : {
      "description" : "The ID of the virtual private gateway that is attached to a VPC. The virtual private gateway must be attached to the same VPC that the routing tables are associated with",
      "type" : "string"
    }
  },
  "required" : [ "RouteTableIds", "VpnGatewayId" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:EnableVgwRoutePropagation", "ec2:DescribeRouteTables" ]
    },
    "update" : {
      "permissions" : [ "ec2:EnableVgwRoutePropagation", "ec2:DescribeRouteTables" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DisableVgwRoutePropagation", "ec2:DescribeRouteTables" ]
    }
  }
}