SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::VpcLink",
  "description" : "The ``AWS::ApiGatewayV2::VpcLink`` resource creates a VPC link. Supported only for HTTP APIs. The VPC link status must transition from ``PENDING`` to ``AVAILABLE`` to successfully create a VPC link, which can take up to 10 minutes. To learn more, see [Working with VPC Links for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html) in the *API Gateway Developer Guide*.",
  "additionalProperties" : False,
  "properties" : {
    "VpcLinkId" : {
      "type" : "string",
      "description" : ""
    },
    "SubnetIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      },
      "description" : "A list of subnet IDs to include in the VPC link."
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      },
      "description" : "A list of security group IDs for the VPC link."
    },
    "Tags" : {
      "type" : "object",
      "description" : "The collection of tags. Each tag element is associated with a given resource.",
      "additionalProperties" : False,
      "patternProperties" : {
        ".*" : {
          "type" : "string"
        }
      }
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the VPC link."
    }
  },
  "required" : [ "SubnetIds", "Name" ],
  "createOnlyProperties" : [ "/properties/SecurityGroupIds", "/properties/SubnetIds" ],
  "primaryIdentifier" : [ "/properties/VpcLinkId" ],
  "readOnlyProperties" : [ "/properties/VpcLinkId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "apigateway:POST", "apigateway:GET", "apigateway:TagResource", "iam:CreateServiceLinkedRole", "iam:DeleteServiceLinkedRole", "iam:GetServiceLinkedRoleDeletionStatus" ]
    },
    "update" : {
      "permissions" : [ "apigateway:PATCH", "apigateway:GET", "apigateway:TagResource", "apigateway:unTagResource", "iam:CreateServiceLinkedRole", "iam:DeleteServiceLinkedRole", "iam:GetServiceLinkedRoleDeletionStatus" ]
    },
    "read" : {
      "permissions" : [ "apigateway:GET", "iam:CreateServiceLinkedRole", "iam:DeleteServiceLinkedRole", "iam:GetServiceLinkedRoleDeletionStatus" ]
    },
    "delete" : {
      "permissions" : [ "apigateway:GET", "apigateway:DELETE", "iam:CreateServiceLinkedRole", "iam:DeleteServiceLinkedRole", "iam:GetServiceLinkedRoleDeletionStatus" ]
    },
    "list" : {
      "permissions" : [ "apigateway:GET", "iam:CreateServiceLinkedRole", "iam:DeleteServiceLinkedRole", "iam:GetServiceLinkedRoleDeletionStatus" ]
    }
  }
}