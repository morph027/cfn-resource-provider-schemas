SCHEMA = {
  "typeName" : "AWS::AppRunner::VpcIngressConnection",
  "description" : "The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apprunner.git",
  "definitions" : {
    "IngressVpcConfiguration" : {
      "description" : "The configuration of customer’s VPC and related VPC endpoint",
      "type" : "object",
      "properties" : {
        "VpcId" : {
          "description" : "The ID of the VPC that the VPC endpoint is used in.",
          "type" : "string"
        },
        "VpcEndpointId" : {
          "description" : "The ID of the VPC endpoint that your App Runner service connects to.",
          "type" : "string"
        }
      },
      "required" : [ "VpcId", "VpcEndpointId" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "VpcIngressConnectionArn" : {
      "description" : "The Amazon Resource Name (ARN) of the VpcIngressConnection.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1011,
      "pattern" : "arn:aws(-[\\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\\w|/|-){1,1011}"
    },
    "VpcIngressConnectionName" : {
      "description" : "The customer-provided Vpc Ingress Connection name.",
      "type" : "string",
      "minLength" : 4,
      "maxLength" : 40,
      "pattern" : "[A-Za-z0-9][A-Za-z0-9\\-_]{3,39}"
    },
    "ServiceArn" : {
      "description" : "The Amazon Resource Name (ARN) of the service.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1011,
      "pattern" : "arn:aws(-[\\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\\w|/|-){1,1011}"
    },
    "Status" : {
      "description" : "The current status of the VpcIngressConnection.",
      "type" : "string",
      "enum" : [ "AVAILABLE", "PENDING_CREATION", "PENDING_UPDATE", "PENDING_DELETION", "FAILED_CREATION", "FAILED_UPDATE", "FAILED_DELETION", "DELETED" ]
    },
    "DomainName" : {
      "description" : "The Domain name associated with the VPC Ingress Connection.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "[A-Za-z0-9*.-]{1,255}"
    },
    "IngressVpcConfiguration" : {
      "$ref" : "#/definitions/IngressVpcConfiguration"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "additionalProperties" : False,
  "required" : [ "ServiceArn", "IngressVpcConfiguration" ],
  "createOnlyProperties" : [ "/properties/VpcIngressConnectionName", "/properties/ServiceArn", "/properties/Tags" ],
  "readOnlyProperties" : [ "/properties/VpcIngressConnectionArn", "/properties/DomainName", "/properties/Status" ],
  "writeOnlyProperties" : [ "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/VpcIngressConnectionArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "apprunner:CreateVpcIngressConnection", "apprunner:DescribeVpcIngressConnection", "ec2:DescribeVpcs", "ec2:DescribeVpcEndpoints", "ec2:DescribeSubnets", "apprunner:TagResource" ]
    },
    "read" : {
      "permissions" : [ "apprunner:DescribeVpcIngressConnection" ]
    },
    "update" : {
      "permissions" : [ "apprunner:UpdateVpcIngressConnection", "apprunner:DescribeVpcIngressConnection", "ec2:DescribeVpcs", "ec2:DescribeVpcEndpoints", "ec2:DescribeSubnets", "apprunner:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "apprunner:DeleteVpcIngressConnection", "apprunner:DescribeVpcIngressConnection" ]
    },
    "list" : {
      "permissions" : [ "apprunner:ListVpcIngressConnections" ]
    }
  }
}