SCHEMA = {
  "tagging" : {
    "permissions" : [ "vpc-lattice:UntagResource", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource" ],
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : True
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "vpc-lattice:GetResourceGateway", "vpc-lattice:ListTagsForResource" ]
    },
    "create" : {
      "permissions" : [ "vpc-lattice:CreateResourceGateway", "vpc-lattice:GetResourceGateway", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:UpdateResourceGateway", "vpc-lattice:GetResourceGateway", "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:ListTagsForResource", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListResourceGateways" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteResourceGateway", "vpc-lattice:GetResourceGateway", "vpc-lattice:UntagResource" ]
    }
  },
  "typeName" : "AWS::VpcLattice::ResourceGateway",
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "description" : "Creates a resource gateway for a service. ",
  "additionalIdentifiers" : [ [ "/properties/Id" ] ],
  "createOnlyProperties" : [ "/properties/VpcIdentifier", "/properties/SubnetIds", "/properties/IpAddressType", "/properties/Name" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Arn" ],
  "definitions" : {
    "Tag" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "minLength" : 1,
          "type" : "string",
          "maxLength" : 256
        },
        "Key" : {
          "minLength" : 1,
          "type" : "string",
          "maxLength" : 128
        }
      },
      "required" : [ "Key" ]
    }
  },
  "properties" : {
    "IpAddressType" : {
      "type" : "string",
      "enum" : [ "IPV4", "IPV6", "DUALSTACK" ]
    },
    "VpcIdentifier" : {
      "minLength" : 5,
      "type" : "string",
      "maxLength" : 50
    },
    "Id" : {
      "minLength" : 17,
      "pattern" : "^((rgw-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:resourcegateway/rgw-[0-9a-z]{17}))$",
      "type" : "string",
      "maxLength" : 2048
    },
    "Arn" : {
      "minLength" : 20,
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:resourcegateway/rgw-[0-9a-z]{17}$",
      "type" : "string",
      "maxLength" : 2048
    },
    "SubnetIds" : {
      "uniqueItems" : True,
      "description" : "The ID of one or more subnets in which to create an endpoint network interface.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "relationshipRef" : {
          "typeName" : "AWS::EC2::Subnet",
          "propertyPath" : "/properties/SubnetId"
        },
        "type" : "string"
      }
    },
    "SecurityGroupIds" : {
      "uniqueItems" : True,
      "description" : "The ID of one or more security groups to associate with the endpoint network interface.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "anyOf" : [ {
          "relationshipRef" : {
            "typeName" : "AWS::EC2::SecurityGroup",
            "propertyPath" : "/properties/GroupId"
          }
        }, {
          "relationshipRef" : {
            "typeName" : "AWS::EC2::SecurityGroup",
            "propertyPath" : "/properties/Id"
          }
        }, {
          "relationshipRef" : {
            "typeName" : "AWS::EC2::VPC",
            "propertyPath" : "/properties/DefaultSecurityGroup"
          }
        } ],
        "type" : "string"
      }
    },
    "Tags" : {
      "minItems" : 0,
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Name" : {
      "minLength" : 3,
      "pattern" : "^(?!rgw-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$",
      "type" : "string",
      "maxLength" : 40
    }
  },
  "required" : [ "Name", "VpcIdentifier", "SubnetIds" ]
}