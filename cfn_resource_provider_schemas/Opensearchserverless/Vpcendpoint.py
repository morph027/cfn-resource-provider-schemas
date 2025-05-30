SCHEMA = {
  "typeName" : "AWS::OpenSearchServerless::VpcEndpoint",
  "description" : "Amazon OpenSearchServerless vpc endpoint resource",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "Id" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^vpce-[0-9a-z]*$",
      "description" : "The identifier of the VPC Endpoint"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 3,
      "pattern" : "^[a-z][a-z0-9-]{2,31}$",
      "description" : "The name of the VPC Endpoint"
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 128,
        "minLength" : 1,
        "pattern" : "^[\\w+\\-]+$"
      },
      "maxItems" : 5,
      "minItems" : 1,
      "description" : "The ID of one or more security groups to associate with the endpoint network interface"
    },
    "SubnetIds" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 32,
        "minLength" : 1,
        "pattern" : "^subnet-([0-9a-f]{8}|[0-9a-f]{17})$"
      },
      "maxItems" : 6,
      "minItems" : 1,
      "description" : "The ID of one or more subnets in which to create an endpoint network interface"
    },
    "VpcId" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^vpc-[0-9a-z]*$",
      "description" : "The ID of the VPC in which the endpoint will be used."
    }
  },
  "required" : [ "Name", "VpcId", "SubnetIds" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/VpcId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/Name" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "aoss:BatchGetVpcEndpoint", "aoss:CreateVpcEndpoint", "ec2:CreateVpcEndpoint", "ec2:DeleteVpcEndPoints", "ec2:DescribeVpcEndpoints", "ec2:ModifyVpcEndPoint", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:CreateTags", "route53:ChangeResourceRecordSets", "route53:GetChange", "route53:GetHostedZone", "route53:ListResourceRecordSets", "route53:ListHostedZonesByName", "route53:CreateHostedZone", "route53:ListHostedZonesByVPC", "route53:AssociateVPCWithHostedZone" ]
    },
    "read" : {
      "permissions" : [ "aoss:BatchGetVpcEndpoint", "ec2:DescribeVpcEndpoints" ]
    },
    "update" : {
      "permissions" : [ "aoss:BatchGetVpcEndpoint", "aoss:UpdateVpcEndpoint", "ec2:CreateVpcEndpoint", "ec2:DeleteVpcEndPoints", "ec2:DescribeVpcEndpoints", "ec2:ModifyVpcEndPoint", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:CreateTags", "route53:ChangeResourceRecordSets", "route53:GetChange", "route53:GetHostedZone", "route53:ListResourceRecordSets", "route53:ListHostedZonesByName", "route53:CreateHostedZone", "route53:ListHostedZonesByVPC", "route53:AssociateVPCWithHostedZone" ]
    },
    "delete" : {
      "permissions" : [ "aoss:BatchGetVpcEndpoint", "aoss:DeleteVpcEndpoint", "ec2:DeleteVpcEndPoints", "ec2:DescribeVpcEndpoints", "ec2:ModifyVpcEndPoint", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:CreateTags", "route53:ChangeResourceRecordSets", "route53:DeleteHostedZone", "route53:GetChange", "route53:GetHostedZone", "route53:ListResourceRecordSets", "route53:ListHostedZonesByName", "route53:ListHostedZonesByVPC", "route53:AssociateVPCWithHostedZone" ]
    },
    "list" : {
      "permissions" : [ "aoss:ListVpcEndpoints", "ec2:DescribeVpcEndpoints" ]
    }
  },
  "additionalProperties" : False
}