SCHEMA = {
  "typeName" : "AWS::RefactorSpaces::Application",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-refactor-spaces",
  "description" : "Definition of AWS::RefactorSpaces::Application Resource Type",
  "definitions" : {
    "ApiGatewayEndpointType" : {
      "type" : "string",
      "enum" : [ "REGIONAL", "PRIVATE" ]
    },
    "ApiGatewayProxyInput" : {
      "type" : "object",
      "properties" : {
        "StageName" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^[-a-zA-Z0-9_]*$"
        },
        "EndpointType" : {
          "$ref" : "#/definitions/ApiGatewayEndpointType"
        }
      },
      "additionalProperties" : False
    },
    "ProxyType" : {
      "type" : "string",
      "enum" : [ "API_GATEWAY" ]
    },
    "Tag" : {
      "description" : "A label for tagging Environment resource",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "A string used to identify this tag",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^(?!aws:).+"
        },
        "Value" : {
          "description" : "A string containing the value for the tag",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ApiGatewayProxy" : {
      "$ref" : "#/definitions/ApiGatewayProxyInput"
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:(aws[a-zA-Z-]*)?:refactor-spaces:[a-zA-Z0-9\\-]+:\\w{12}:[a-zA-Z_0-9+=,.@\\-_/]+$"
    },
    "ApiGatewayId" : {
      "type" : "string",
      "maxLength" : 10,
      "minLength" : 10,
      "pattern" : "^[a-z0-9]{10}$"
    },
    "VpcLinkId" : {
      "type" : "string",
      "maxLength" : 10,
      "minLength" : 10,
      "pattern" : "^[a-z0-9]{10}$"
    },
    "NlbArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:(aws[a-zA-Z-]*)?:elasticloadbalancing:[a-zA-Z0-9\\\\-]+:\\\\w{12}:[a-zA-Z_0-9+=,.@\\\\-_\\/]+$"
    },
    "NlbName" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 1,
      "pattern" : "^(?!internal-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+.*[^-]$"
    },
    "ApplicationIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^app-([0-9A-Za-z]{10}$)"
    },
    "EnvironmentIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^env-([0-9A-Za-z]{10}$)"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "^(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$"
    },
    "ProxyType" : {
      "$ref" : "#/definitions/ProxyType"
    },
    "VpcId" : {
      "type" : "string",
      "maxLength" : 21,
      "minLength" : 12,
      "pattern" : "^vpc-[-a-f0-9]{8}([-a-f0-9]{9})?$"
    },
    "StageName" : {
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 1,
      "pattern" : "^[-a-zA-Z0-9_]*$"
    },
    "ProxyUrl" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "pattern" : "^http://[-a-zA-Z0-9+\\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\\x38@#/%=~_|]$"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "description" : "Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair."
    }
  },
  "required" : [ "EnvironmentIdentifier", "VpcId", "Name", "ProxyType" ],
  "readOnlyProperties" : [ "/properties/ApplicationIdentifier", "/properties/Arn", "/properties/ApiGatewayId", "/properties/VpcLinkId", "/properties/NlbArn", "/properties/NlbName", "/properties/ProxyUrl", "/properties/StageName" ],
  "writeOnlyProperties" : [ "/properties/ApiGatewayProxy" ],
  "createOnlyProperties" : [ "/properties/ApiGatewayProxy", "/properties/EnvironmentIdentifier", "/properties/Name", "/properties/ProxyType", "/properties/VpcId" ],
  "primaryIdentifier" : [ "/properties/EnvironmentIdentifier", "/properties/ApplicationIdentifier" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "refactor-spaces:GetApplication", "refactor-spaces:CreateApplication", "refactor-spaces:TagResource", "ec2:CreateTags", "ec2:CreateVpcEndpointServiceConfiguration", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeVpcEndpointServiceConfigurations", "ec2:DescribeAccountAttributes", "ec2:DescribeInternetGateways", "ec2:ModifyVpcEndpointServicePermissions", "apigateway:DELETE", "apigateway:GET", "apigateway:PATCH", "apigateway:POST", "apigateway:PUT", "apigateway:UpdateRestApiPolicy", "elasticloadbalancing:CreateLoadBalancer", "elasticloadbalancing:DescribeLoadBalancers", "elasticloadbalancing:DescribeTags", "elasticloadbalancing:AddTags", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "refactor-spaces:GetApplication", "refactor-spaces:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "refactor-spaces:GetApplication", "refactor-spaces:DeleteApplication", "refactor-spaces:UntagResource", "ec2:DescribeVpcEndpointServiceConfigurations", "ec2:DeleteRoute", "ec2:DeleteSecurityGroup", "ec2:DeleteTransitGateway", "ec2:DeleteTransitGatewayVpcAttachment", "ec2:DeleteVpcEndpointServiceConfigurations", "ec2:DeleteTags", "ec2:RevokeSecurityGroupIngress", "elasticloadbalancing:DeleteLoadBalancer", "apigateway:DELETE", "apigateway:GET", "apigateway:PUT", "apigateway:UpdateRestApiPolicy" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "EnvironmentIdentifier" : {
            "$ref" : "resource-schema.json#/properties/EnvironmentIdentifier"
          }
        },
        "required" : [ "EnvironmentIdentifier" ]
      },
      "permissions" : [ "refactor-spaces:ListApplications", "refactor-spaces:ListTagsForResource" ]
    }
  },
  "taggable" : True
}