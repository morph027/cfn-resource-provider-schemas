SCHEMA = {
  "typeName" : "AWS::EC2::Route",
  "description" : "Specifies a route in a route table. For more information, see [Routes](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-table-routes) in the *Amazon VPC User Guide*.\n You must specify either a destination CIDR block or prefix list ID. You must also specify exactly one of the resources as the target.\n If you create a route that references a transit gateway in the same template where you create the transit gateway, you must declare a dependency on the transit gateway attachment. The route table cannot use the transit gateway until it has successfully attached to the VPC. Add a [DependsOn Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) in the ``AWS::EC2::Route`` resource to explicitly declare a dependency on the ``AWS::EC2::TransitGatewayAttachment`` resource.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2",
  "additionalProperties" : False,
  "properties" : {
    "CarrierGatewayId" : {
      "type" : "string",
      "description" : "The ID of the carrier gateway.\n You can only use this option when the VPC contains a subnet which is associated with a Wavelength Zone."
    },
    "CidrBlock" : {
      "type" : "string",
      "description" : ""
    },
    "CoreNetworkArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the core network."
    },
    "DestinationCidrBlock" : {
      "type" : "string",
      "description" : "The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18/18``, we modify it to ``100.68.0.0/18``."
    },
    "DestinationIpv6CidrBlock" : {
      "type" : "string",
      "description" : "The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match."
    },
    "DestinationPrefixListId" : {
      "type" : "string",
      "description" : "The ID of a prefix list used for the destination match."
    },
    "EgressOnlyInternetGatewayId" : {
      "type" : "string",
      "description" : "[IPv6 traffic only] The ID of an egress-only internet gateway."
    },
    "GatewayId" : {
      "type" : "string",
      "description" : "The ID of an internet gateway or virtual private gateway attached to your VPC."
    },
    "InstanceId" : {
      "type" : "string",
      "description" : "The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached."
    },
    "LocalGatewayId" : {
      "type" : "string",
      "description" : "The ID of the local gateway."
    },
    "NatGatewayId" : {
      "type" : "string",
      "description" : "[IPv4 traffic only] The ID of a NAT gateway."
    },
    "NetworkInterfaceId" : {
      "type" : "string",
      "description" : "The ID of a network interface."
    },
    "RouteTableId" : {
      "type" : "string",
      "description" : "The ID of the route table for the route."
    },
    "TransitGatewayId" : {
      "type" : "string",
      "description" : "The ID of a transit gateway."
    },
    "VpcEndpointId" : {
      "type" : "string",
      "description" : "The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only."
    },
    "VpcPeeringConnectionId" : {
      "type" : "string",
      "description" : "The ID of a VPC peering connection."
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "RouteTableId" ],
  "readOnlyProperties" : [ "/properties/CidrBlock" ],
  "createOnlyProperties" : [ "/properties/RouteTableId", "/properties/DestinationCidrBlock", "/properties/DestinationIpv6CidrBlock", "/properties/DestinationPrefixListId" ],
  "primaryIdentifier" : [ "/properties/RouteTableId", "/properties/CidrBlock" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateRoute", "ec2:DescribeRouteTables", "ec2:DescribeNetworkInterfaces" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeRouteTables" ]
    },
    "update" : {
      "permissions" : [ "ec2:ReplaceRoute", "ec2:DescribeRouteTables", "ec2:DescribeNetworkInterfaces" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteRoute", "ec2:DescribeRouteTables" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeRouteTables" ],
      "handlerSchema" : {
        "properties" : {
          "RouteTableId" : {
            "$ref" : "resource-schema.json#/properties/RouteTableId"
          }
        },
        "required" : [ "RouteTableId" ]
      }
    }
  }
}