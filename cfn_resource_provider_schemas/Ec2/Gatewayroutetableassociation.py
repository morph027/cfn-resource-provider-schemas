SCHEMA = {
  "typeName" : "AWS::EC2::GatewayRouteTableAssociation",
  "description" : "Associates a gateway with a route table. The gateway and route table must be in the same VPC. This association causes the incoming traffic to the gateway to be routed according to the routes in the route table.",
  "sourceUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html",
  "properties" : {
    "RouteTableId" : {
      "description" : "The ID of the route table.",
      "type" : "string"
    },
    "GatewayId" : {
      "description" : "The ID of the gateway.",
      "type" : "string"
    },
    "AssociationId" : {
      "description" : "The route table association ID.",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "RouteTableId", "GatewayId" ],
  "primaryIdentifier" : [ "/properties/GatewayId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:DescribeRouteTables", "ec2:AssociateRouteTable" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeRouteTables" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeRouteTables", "ec2:ReplaceRouteTableAssociation" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DescribeRouteTables", "ec2:DisassociateRouteTable" ]
    }
  },
  "createOnlyProperties" : [ "/properties/GatewayId" ],
  "readOnlyProperties" : [ "/properties/AssociationId" ]
}