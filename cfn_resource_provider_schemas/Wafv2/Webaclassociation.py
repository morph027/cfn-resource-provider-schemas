SCHEMA = {
  "typeName" : "AWS::WAFv2::WebACLAssociation",
  "description" : "Associates WebACL to Application Load Balancer, CloudFront or API Gateway.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-wafv2.git",
  "definitions" : {
    "ResourceArn" : {
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
    }
  },
  "properties" : {
    "ResourceArn" : {
      "$ref" : "#/definitions/ResourceArn"
    },
    "WebACLArn" : {
      "$ref" : "#/definitions/ResourceArn"
    }
  },
  "required" : [ "ResourceArn", "WebACLArn" ],
  "createOnlyProperties" : [ "/properties/ResourceArn", "/properties/WebACLArn" ],
  "primaryIdentifier" : [ "/properties/ResourceArn", "/properties/WebACLArn" ],
  "additionalProperties" : False,
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "wafv2:AssociateWebACL", "wafv2:GetWebACLForResource", "wafv2:GetWebACL", "wafv2:DisassociateWebACL", "wafv2:PutPermissionPolicy", "wafv2:GetPermissionPolicy", "elasticloadbalancing:SetWebACL", "apigateway:SetWebACL", "appsync:SetWebACL", "cognito-idp:AssociateWebACL", "cognito-idp:DisassociateWebACL", "cognito-idp:GetWebACLForResource", "apprunner:AssociateWebAcl", "apprunner:DisassociateWebAcl", "apprunner:DescribeWebAclForService", "ec2:AssociateVerifiedAccessInstanceWebAcl", "ec2:DisassociateVerifiedAccessInstanceWebAcl", "ec2:DescribeVerifiedAccessInstanceWebAclAssociations", "ec2:GetVerifiedAccessInstanceWebAcl", "amplify:AssociateWebACL", "amplify:GetWebACLForResource" ]
    },
    "delete" : {
      "permissions" : [ "wafv2:AssociateWebACL", "wafv2:GetWebACLForResource", "wafv2:GetWebACL", "wafv2:DisassociateWebACL", "wafv2:PutPermissionPolicy", "elasticloadbalancing:SetWebACL", "apigateway:SetWebACL", "appsync:SetWebACL", "cognito-idp:AssociateWebACL", "cognito-idp:DisassociateWebACL", "cognito-idp:GetWebACLForResource", "apprunner:AssociateWebAcl", "apprunner:DisassociateWebAcl", "apprunner:DescribeWebAclForService", "ec2:AssociateVerifiedAccessInstanceWebAcl", "ec2:DisassociateVerifiedAccessInstanceWebAcl", "ec2:DescribeVerifiedAccessInstanceWebAclAssociations", "ec2:GetVerifiedAccessInstanceWebAcl", "amplify:DisassociateWebACL", "amplify:GetWebACLForResource" ]
    },
    "read" : {
      "permissions" : [ "wafv2:AssociateWebACL", "wafv2:GetWebACLForResource", "wafv2:GetWebACL", "wafv2:DisassociateWebACL", "elasticloadbalancing:SetWebACL", "apigateway:SetWebACL", "appsync:SetWebACL", "cognito-idp:AssociateWebACL", "cognito-idp:DisassociateWebACL", "cognito-idp:GetWebACLForResource", "apprunner:AssociateWebAcl", "apprunner:DisassociateWebAcl", "apprunner:DescribeWebAclForService", "ec2:AssociateVerifiedAccessInstanceWebAcl", "ec2:DisassociateVerifiedAccessInstanceWebAcl", "ec2:DescribeVerifiedAccessInstanceWebAclAssociations", "ec2:GetVerifiedAccessInstanceWebAcl", "amplify:GetWebACLForResource" ]
    },
    "update" : {
      "permissions" : [ "wafv2:AssociateWebACL", "wafv2:GetWebACLForResource", "wafv2:GetWebACL", "wafv2:DisassociateWebACL", "elasticloadbalancing:SetWebACL", "apigateway:SetWebACL", "appsync:SetWebACL", "cognito-idp:AssociateWebACL", "cognito-idp:DisassociateWebACL", "cognito-idp:GetWebACLForResource", "apprunner:AssociateWebAcl", "apprunner:DisassociateWebAcl", "apprunner:DescribeWebAclForService", "ec2:AssociateVerifiedAccessInstanceWebAcl", "ec2:DisassociateVerifiedAccessInstanceWebAcl", "ec2:DescribeVerifiedAccessInstanceWebAclAssociations", "ec2:GetVerifiedAccessInstanceWebAcl" ]
    }
  }
}